#!/bin/bash

to_source=$(dirname "$(readlink -f "$0")")
cd "$to_source" || exit

if [ $# != 1 ]; then
	echo Usage: ./build_debug_asan.sh file-name
	exit 1
fi

clang -std=c99 -Wall -Werror -fsanitize=address -fno-omit-frame-pointer -g "$1" -o build_debug_asan
