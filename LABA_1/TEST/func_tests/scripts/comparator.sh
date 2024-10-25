#!/bin/bash

file_1=$1
file_2=$2 

touch save_line_1.txt
touch save_line_2.txt
create_line=""

if [ -e "$file_1" ] && [ -e "$file_2" ]; then
	lines_1=$(cat "$file_1")
	lines_2=$(cat "$file_2")
	for line in $lines_1
	do
		create_line+="${line} "
	done
	echo "$create_line" 1> save_line_1.txt
	
	create_line=""
	for line in $lines_2
	do
		create_line+="${line} "
	done
	echo "$create_line" 1> save_line_2.txt
	if diff save_line_1.txt save_line_2.txt; then
		exit 0
	else
		exit 1
	fi 
else
    exit 1
fi
