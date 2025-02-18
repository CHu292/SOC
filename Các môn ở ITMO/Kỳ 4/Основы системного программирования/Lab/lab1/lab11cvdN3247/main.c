#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <sys/stat.h>
#include <unistd.h>
#include <getopt.h>

#define MAX_PATH_LENGTH 1024

// Function to check if a file contains a specific byte sequence
int file_contains(const char *filename, const char *search_target) {
    FILE *file = fopen(filename, "rb");
    if (!file) {
        perror("Error opening file");
        return 0;
    }

    // Get file size
    fseek(file, 0, SEEK_END);
    long file_size = ftell(file);
    fseek(file, 0, SEEK_SET);

    // Allocate memory to store file content
    char *file_content = (char *)malloc((size_t)file_size + 1); // Add 1 for null terminator
    if (!file_content) {
        fclose(file);
        perror("Error allocating memory");
        return 0;
    }

    // Read file content
    if (fread(file_content, 1, (size_t)file_size, file) != (size_t)file_size) {
        fclose(file);
        free(file_content);
        perror("Error reading file");
        return 0;
    }
    file_content[file_size] = '\0'; // Null-terminate the string
    fclose(file);

    // Search for the target sequence
    char *found = strstr(file_content, search_target);
    free(file_content);
    return (found != NULL);
}

// Function to recursively search files in a directory
void search_directory(const char *path, const char *search_target) {
    DIR *dir;
    struct dirent *entry;
    char full_path[MAX_PATH_LENGTH];

    dir = opendir(path);
    if (!dir) {
        perror("Error opening directory");
        return;
    }

    while ((entry = readdir(dir)) != NULL) {
        if (strcmp(entry->d_name, ".") == 0 || strcmp(entry->d_name, "..") == 0)
            continue;

        snprintf(full_path, MAX_PATH_LENGTH, "%s/%s", path, entry->d_name);

        struct stat statbuf;
        if (stat(full_path, &statbuf) == -1) {
            perror("Error stating file");
            continue;
        }

        if (S_ISDIR(statbuf.st_mode)) {
            search_directory(full_path, search_target);
        } else {
            if (file_contains(full_path, search_target)) {
                printf("%s\n", full_path);
            }
        }
    }

    closedir(dir);
}

int main(int argc, char *argv[]) {
    int opt;
    int help_flag = 0, version_flag = 0;

    // Parse command line options
    static struct option long_options[] = {
        {"help", no_argument, 0, 'h'},
        {"version", no_argument, 0, 'v'},
        {0, 0, 0, 0}
    };

    while ((opt = getopt_long(argc, argv, "hv", long_options, NULL)) != -1) {
        switch (opt) {
            case 'h':
                help_flag = 1;
                break;
            case 'v':
                version_flag = 1;
                break;
            default:
                fprintf(stderr, "Usage: %s [OPTION]... DIRECTORY SEARCH_TARGET\n", argv[0]);
                exit(EXIT_FAILURE);
        }
    }

    if (help_flag) {
        printf("Help information...\n");
        exit(EXIT_SUCCESS);
    }

    if (version_flag) {
        printf("Version information: Lab11cvdN3247\n");
        exit(EXIT_SUCCESS);
    }

    if (optind >= argc - 1) {
        fprintf(stderr, "Usage: %s [OPTION]... DIRECTORY SEARCH_TARGET\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    const char *directory = argv[optind];
    const char *search_target = argv[optind + 1];

    // Perform recursive search in the specified directory
    search_directory(directory, search_target);

    return 0;
}
