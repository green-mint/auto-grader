CC=gcc
CFLAGS=-Wall -g

BINS=1 2 3 4
all: $(BINS)

%: %.c
	$(CC) $(CFLAGS) $^ -o $@

clean:
	rm $(BINS)