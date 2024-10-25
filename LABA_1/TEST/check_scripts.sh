#!/bin/bash

to_source=$(dirname "$(readlink -f "$0")")
cd "$to_source" || exit
bash build_debug_asan.sh main.c
bash build_debug_msan.sh main.c
bash build_debug_ubsan.sh main.c
