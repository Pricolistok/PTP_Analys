#!/bin/bash

to_source=$(dirname "$(readlink -f "$0")")
cd "$to_source" || exit
"./clean.sh"
"./build_coverage.sh"
"./func_tests/scripts/func_tests.sh"
gcov ./main.c
