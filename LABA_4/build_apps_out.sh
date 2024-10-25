#!/bin/bash

## Определяем начальное и конечное значение
settings_file="./settings.txt"
start_val=$(cut -f 2 -d ' ' "$settings_file")
finish_val=$(cut -f 4 -d ' ' "$settings_file")
step=$(cut -f 6 -d ' ' "$settings_file")
c_files="_formal _index _point"

## Создание исполняемых файлов
for c_file in $c_files; 
do
    for (( j=start_val; j<=finish_val; j+=step )); 
    do
        gcc -std=c99 -Wall -Werror -Wpedantic -Wextra -Wvla -Wfloat-conversion -Wfloat-equal -O0 -o ./apps_out/app"${c_file}"/"${j}".exe  c_files_out/main"${c_file}".c -DN=$j -lm
    done
done

