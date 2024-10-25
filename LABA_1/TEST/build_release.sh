#!/bin/bash

to_source=$(dirname "$(readlink -f "$0")")
cd "$to_source" || exit

gcc -std=c99 -Wall -Werror -Wextra -Wfloat-equal -Wfloat-conversion -Wpedantic -c main.c
gcc -o app.exe main.c -lm
