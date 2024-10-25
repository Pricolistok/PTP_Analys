#!/bin/bash
if [ $# != 2 ]; then
	echo Error
	exit 1
fi
echo "$1" > save_in.txt
touch save_res.txt
start_file=$(find "../../" -name "app.exe")
"$start_file" < save_in.txt > save_res.txt
if [ $? -eq 1 ]; then
	rm save_in.txt
	rm save_res.txt
	exit 0
fi
rm save_in.txt
rm save_res.txt
exit 1
