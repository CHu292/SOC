#ifndef PLUGIN_API_H
#define PLUGIN_API_H

#include <stdio.h>

// Структура для хранения информации о параметрах plugin
typedef struct {
    const char *option_name;   // Tên tùy chọn
    const char *description;   // Mô tả tùy chọn
} plugin_option_t;

// Функция для получения информации о параметрах plugin
typedef void (*plugin_get_info_t)(plugin_option_t **options, int *num_options);

// Функция для обработки файлов и проверки состояния plugin
typedef int (*plugin_process_file_t)(const char *filename, const char *arg);

#endif // PLUGIN_API_H
