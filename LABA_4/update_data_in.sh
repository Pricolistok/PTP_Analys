#!/bin/bash

## Определяем начальное и конечное значение массива
settings_file="./settings.txt"
start_val=$(cut -f 2 -d ' ' "$settings_file")
finish_val=$(cut -f 4 -d ' ' "$settings_file")
step=$(cut -f 6 -d ' ' "$settings_file")
c_files="_formal _index _point"

## Запуск каждого файла и перенаправление результатов в текстовые файлы
for c_file in $c_files; 
do
    for (( i=start_val; i<=finish_val; i+=step )); 
    do
        gcc -std=c99 -Wall -Werror -Wpedantic -Wextra -Wvla -Wfloat-conversion -Wfloat-equal -O0 -o ./app_in/app.exe  c_files_in/main"${c_file}".c -DN=$i -lm
        ./app_in/app.exe >> ./data_in/data"${c_file}"/${i}.txt
    done
done

## Запуск каждого файла и перенаправление результатов в текстовые файлы
for c_file in $c_files; 
do
    for (( i=start_val; i<=finish_val; i+=step )); 
    do
        gcc -std=c99 -Wall -Werror -Wpedantic -Wextra -Wvla -Wfloat-conversion -Wfloat-equal -O0 -o ./app_in/app_tsc.exe  c_files_in/main"${c_file}_tsc".c -DN=$i -lm
        ./app_in/app_tsc.exe >> ./data_in/data"${c_file}_tsc"/${i}.txt
    done
done

