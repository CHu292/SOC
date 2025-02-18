#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "plugin_api.h"

static unsigned short crc16_ccitt(const unsigned char *data, size_t length) {
    unsigned short crc = 0xFFFF;
    for (size_t i = 0; i < length; i++) {
        crc ^= (unsigned short)data[i] << 8;
        for (unsigned char j = 0; j < 8; j++) {
            if (crc & 0x8000) {
                crc = (crc << 1) ^ 0x1021;
            } else {
                crc = crc << 1;
            }
        }
    }
    return crc;
}

static int process_file(const char *filename, const char *arg) {
    FILE *file = fopen(filename, "rb");
    if (!file) {
        perror("Error opening file");
        return 0;
    }

    fseek(file, 0, SEEK_END);
    long file_size = ftell(file);
    fseek(file, 0, SEEK_SET);

    unsigned char *file_content = malloc(file_size);
    if (!file_content) {
        fclose(file);
        perror("Error allocating memory");
        return 0;
    }

    fread(file_content, 1, file_size, file);
    fclose(file);

    unsigned short crc = crc16_ccitt(file_content, file_size);
    free(file_content);

    unsigned short target_crc = (unsigned short)strtol(arg, NULL, 0);

    return crc == target_crc;
}

static void get_info(plugin_option_t **options, int *num_options) {
    static plugin_option_t opts[] = {
        {"crc16", "Search files with specified CRC-16-CCITT checksum"}
    };
    *options = opts;
    *num_options = sizeof(opts) / sizeof(plugin_option_t);
}

// Определить функции, чтобы плагин мог использоваться основной программой
__attribute__((visibility("default"))) void plugin_get_info(plugin_option_t **options, int *num_options) {
    get_info(options, num_options);
}

__attribute__((visibility("default"))) int plugin_process_file(const char *filename, const char *arg) {
    return process_file(filename, arg);
}
