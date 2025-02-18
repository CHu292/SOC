CC = gcc
CFLAGS = -Wall -Wextra -fPIC -Iinclude
LDFLAGS = -ldl

PLUGIN_NAME = libcvdN3247.so
PLUGIN_SRC = src/plugin_crc16.c
PLUGIN_OBJ = $(PLUGIN_SRC:.c=.o)

MAIN = lab1cvdN3247
MAIN_SRC = src/main.c
MAIN_OBJ = $(MAIN_SRC:.c=.o)

all: $(MAIN) $(PLUGIN_NAME)

$(MAIN): $(MAIN_OBJ)
	$(CC) $(MAIN_OBJ) $(LDFLAGS) -o $(MAIN)

$(PLUGIN_NAME): $(PLUGIN_OBJ)
	$(CC) $(CFLAGS) -shared -o plugins/$(PLUGIN_NAME) $(PLUGIN_OBJ)

clean:
	rm -f $(MAIN) $(MAIN_OBJ) $(PLUGIN_OBJ) plugins/$(PLUGIN_NAME)

.PHONY: all clean
