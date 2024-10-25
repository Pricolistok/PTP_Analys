#!/bin/bash

## Определяем начальное и конечное значение массива
settings_file="./settings.txt"
start_val=$(cut -f 2 -d ' ' "$settings_file")
finish_val=$(cut -f 4 -d ' ' "$settings_file")
step=$(cut -f 6 -d ' ' "$settings_file")
count=$(cut -f 8 -d ' ' "$settings_file")
c_files="_formal _index _point"


## Запуск каждого файла и запись результатов
for c_file in $c_files; 
do
    for (( i=start_val; i<=finish_val; i+=step )); 
    do
        for (( j=0; j<count; j++ ));\
        do
            ./apps_out/app"${c_file}"/"${i}".exe >> ./data_out/data"${c_file}"/"${i}".txt
        done
        python3 cnt_rse.py ./data_out/data"${c_file}"/"${i}".txt
        saver=$?
        while [ $saver == 1 ];
        do
            ./apps_out/app"${c_file}"/"${i}".exe >> ./data_out/data"${c_file}"/"${i}".txt
            python3 cnt_rse.py ./data_out/data"${c_file}"/"${i}".txt
            saver=$?
        done
    done
done