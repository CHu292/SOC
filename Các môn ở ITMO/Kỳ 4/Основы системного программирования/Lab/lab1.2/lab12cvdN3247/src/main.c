#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dlfcn.h>
#include <dirent.h>
#include <sys/stat.h>
#include <unistd.h>
#include <getopt.h>
#include "plugin_api.h"

#define MAX_PATH_LENGTH 1024

typedef struct {
    void *handle;
    plugin_process_file_t process_file;
    const char *arg;
} plugin_t;

plugin_t *plugins = NULL;
int plugin_count = 0;
int combine_and = 1;
int negate_search = 0;

void load_plugins(const char *plugin_dir) {
    DIR *dir = opendir(plugin_dir);
    if (!dir) {
        perror("Error opening plugin directory");
        exit(EXIT_FAILURE);
    }

    struct dirent *entry;
    while ((entry = readdir(dir)) != NULL) {
        if (strstr(entry->d_name, ".so")) {
            char full_path[MAX_PATH_LENGTH];
            snprintf(full_path, MAX_PATH_LENGTH, "%s/%s", plugin_dir, entry->d_name);

            void *handle = dlopen(full_path, RTLD_LAZY);
            if (!handle) {
                fprintf(stderr, "Error loading plugin %s: %s\n", full_path, dlerror());
                continue;
            }

            plugin_get_info_t get_info = (plugin_get_info_t)dlsym(handle, "plugin_get_info");
            if (!get_info) {
                fprintf(stderr, "Error finding symbol plugin_get_info in %s: %s\n", full_path, dlerror());
                dlclose(handle);
                continue;
            }

            plugin_process_file_t process_file = (plugin_process_file_t)dlsym(handle, "plugin_process_file");
            if (!process_file) {
                fprintf(stderr, "Error finding symbol plugin_process_file in %s: %s\n", full_path, dlerror());
                dlclose(handle);
                continue;
            }

            plugin_option_t *options;
            int num_options;
            get_info(&options, &num_options);

            for (int i = 0; i < num_options; i++) {
                plugins = realloc(plugins, (plugin_count + 1) * sizeof(plugin_t));
                plugins[plugin_count].handle = handle;
                plugins[plugin_count].process_file = process_file;
                plugins[plugin_count].arg = NULL;  // Set later based on user input
                plugin_count++;
            }
        }
    }

    closedir(dir);
}

int check_file(const char *filename) {
    int result = combine_and ? 1 : 0;

    for (int i = 0; i < plugin_count; i++) {
        int match = plugins[i].process_file(filename, plugins[i].arg);
        if (combine_and) {
            result &= match;
        } else {
            result |= match;
        }
    }

    if (negate_search) {
        result = !result;
    }

    return result;
}

void search_directory(const char *path) {
    DIR *dir = opendir(path);
    if (!dir) {
        perror("Error opening directory");
        return;
    }

    struct dirent *entry;
    char full_path[MAX_PATH_LENGTH];

    while ((entry = readdir(dir)) != NULL) {
        if (strcmp(entry->d_name, ".") == 0 || strcmp(entry->d_name, "..") == 0) {
            continue;
        }

        snprintf(full_path, MAX_PATH_LENGTH, "%s/%s", path, entry->d_name);
        struct stat statbuf;
        if (stat(full_path, &statbuf) == -1) {
            perror("Error stating file");
            continue;
        }

        if (S_ISDIR(statbuf.st_mode)) {
            search_directory(full_path);
        } else {
            if (check_file(full_path)) {
                printf("%s\n", full_path);
            }
        }
    }

    closedir(dir);
}

void print_help() {
    printf("Usage: lab1cvdN3247 [options] [directory]\n");
    printf("Options:\n");
    printf("  -P, --plugin-dir <dir>    Directory containing plugins\n");
    printf("  -A, --and                 Combine search criteria using AND (default)\n");
    printf("  -O, --or                  Combine search criteria using OR\n");
    printf("  -N, --negate              Negate the search criteria\n");
    printf("  -v, --version             Show version information\n");
    printf("  -h, --help                Show this help message\n");
}

void print_version() {
    printf("lab1cvdN3247 version 1.0\n");
    printf("Author: Your Name\n");
    printf("Group: 3247\n");
    printf("Lab Option: --crc16 <value>\n");
}

int main(int argc, char *argv[]) {
    const char *plugin_dir = ".";
    const char *search_dir = NULL;

    static struct option long_options[] = {
        {"plugin-dir", required_argument, 0, 'P'},
        {"and", no_argument, 0, 'A'},
        {"or", no_argument, 0, 'O'},
        {"negate", no_argument, 0, 'N'},
        {"version", no_argument, 0, 'v'},
        {"help", no_argument, 0, 'h'},
        {0, 0, 0, 0}
    };

    int opt;
    while ((opt = getopt_long(argc, argv, "P:AONvh", long_options, NULL)) != -1) {
        switch (opt) {
            case 'P':
                plugin_dir = optarg;
                break;
            case 'A':
                combine_and = 1;
                break;
            case 'O':
                combine_and = 0;
                break;
            case 'N':
                negate_search = 1;
                break;
            case 'v':
                print_version();
                exit(EXIT_SUCCESS);
            case 'h':
                print_help();
                exit(EXIT_SUCCESS);
            default:
                print_help();
                exit(EXIT_FAILURE);
        }
    }

    if (optind < argc) {
        search_dir = argv[optind];
    }

    load_plugins(plugin_dir);

    if (!search_dir) {
        print_help();
        printf("\nAvailable plugins:\n");
        for (int i = 0; i < plugin_count; i++) {
            plugin_option_t *options;
            int num_options;
            plugin_get_info_t get_info = (plugin_get_info_t)dlsym(plugins[i].handle, "plugin_get_info");
            if (get_info) {
                get_info(&options, &num_options);
                for (int j = 0; j < num_options; j++) {
                    printf("  --%s: %s\n", options[j].option_name, options[j].description);
                }
            }
        }
        exit(EXIT_SUCCESS);
    }

    search_directory(search_dir);

    for (int i = 0; i < plugin_count; i++) {
        dlclose(plugins[i].handle);
    }

    free(plugins);

    return 0;
}
