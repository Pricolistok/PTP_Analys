#!/bin/bash

to_source=$(dirname "$(readlink -f "$0")")
cd "$to_source" || exit

rm -f ./*.exe
rm -f ./*.o
rm -f ./*.gcno
rm -f ./*.c.gcov
rm -f ./*.gcda
