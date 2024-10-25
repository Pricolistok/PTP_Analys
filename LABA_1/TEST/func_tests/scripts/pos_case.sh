#!/bin/bash
if [ $# != 2 ]; then
	echo Error
	exit 1
fi
echo "$1" > save_in.txt
echo "$2" > save_out.txt
touch save_res.txt
start_file=$(find "../../" -name "app.exe")
"$start_file" < save_in.txt > save_res.txt
bash comparator.sh save_res.txt save_out.txt
if  ! bash comparator.sh save_res.txt save_out.txt; then
	rm save_in.txt
	rm save_out.txt
	rm save_res.txt
	rm save_line_1.txt
	rm save_line_2.txt
	exit 1
fi
rm save_in.txt
rm save_out.txt
rm save_res.txt
rm save_line_1.txt
rm save_line_2.txt
exit 0
