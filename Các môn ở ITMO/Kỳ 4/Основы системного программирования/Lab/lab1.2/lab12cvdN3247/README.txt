
lab1cvdN3247/
├── include/
│   └── plugin_api.h
├── plugins/
│   └── libcvdN3247.so (создано Makefile)
├── src/
│   ├── main.c
│   └── plugin_crc16.c
├── Makefile
└── README.txt
========================

This project implements a recursive file search utility with dynamic plugin support.

Building the Project:
---------------------
To build the project, run:
    make all

To clean the build artifacts, run:
    make clean

Running the Project:
--------------------
To run the project, use the following command:
    ./lab1cvdN3247 [options] [directory]

Options:
    -P, --plugin-dir <dir>    Directory containing plugins
    -A, --and                 Combine search criteria using AND (default)
    -O, --or                  Combine search criteria using OR
    -N, --negate              Negate the search criteria
    -v, --version             Show version information
    -h, --help                Show this help message

Example:
    ./lab1cvdN3247 -P plugins -A -N /path/to/search

Plugins:
--------
The plugins should be placed in the `plugins` directory or specified directory with -P option.

Plugin Example:
    libcvdN3247.so: Supports --crc16 <value> option to search files with a specified CRC-16-CCITT checksum.
