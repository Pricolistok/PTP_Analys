#!/bin/bash

to_source=$(dirname "$(readlink -f "$0")")
cd "$to_source" || exit

if [ $# != 1 ]; then
  echo Usage: ./msan.sh file-name
  exit 1
fi

clang -std=c99 -Wall -fsanitize=memory -fPIE -pie -fno-omit-frame-pointer -g "$1" -o test_msan
