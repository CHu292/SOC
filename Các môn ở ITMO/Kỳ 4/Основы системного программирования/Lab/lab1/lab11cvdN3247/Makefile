CC = gcc
CFLAGS = -Wall -Wextra -Werror
TARGET = lab11cvdN3247

.PHONY: all clean

all: $(TARGET)

$(TARGET): main.o
	$(CC) $(CFLAGS) -o $@ $^

main.o: main.c
	$(CC) $(CFLAGS) -c -o $@ $<

clean:
	rm -f $(TARGET) *.o