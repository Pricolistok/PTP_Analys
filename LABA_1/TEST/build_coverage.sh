#!/bin/bash

to_source=$(dirname "$(readlink -f "$0")")
cd "$to_source" || exit 1

gcc -std=c99 -Wall -Werror -Wextra -Wfloat-equal -Wfloat-conversion -Wpedantic --coverage -c main.c -o main.o
gcc --coverage -o app.exe main.o -lm