#!/bin/bash

to_source=$(dirname "$(readlink -f "$0")")
cd "$to_source" || exit

ls "$to_source/../data" > save_all.txt
count_files_in=$(grep -Ec 'pos_[0-9]{1,2}_in\.txt' "save_all.txt")
count_files_out=$(grep -Ec 'pos_[0-9]{1,2}_out\.txt' "save_all.txt")
if [ "$count_files_in" -eq "$count_files_out" ]; 
then
  if [ "$count_files_in" -ne 0 ]; 
    then
    for ((i=1; i < count_files_in + 1; i++ ))
    do
      if [ "$i" -lt 10 ];
      then
        data_in=$(cat "../data/pos_0${i}_in.txt")
        data_out=$(cat "../data/pos_0${i}_out.txt")
        bash pos_case.sh "$data_in" "$data_out"
        if [ $? -eq 1 ]; then
          rm save_all.txt
          echo "pos_0$i - ERROR"
          echo 1
          exit 1
        else
          echo "pos_0$i - OK"
        fi
      else
        data_in=$(cat "../data/pos_${i}_in.txt")
        data_out=$(cat "../data/pos_${i}_out.txt")
        bash pos_case.sh "$data_in $data_out"
        if [ $? -eq 1 ]; then
          rm save_all.txt 
          echo "pos_$i - ERROR"
          echo 1
          exit 1

        else
          echo "pos_$i - OK"
        fi
      fi
    done
  fi
else
  rm save_all.txt
  echo 1
  exit 1
fi
count_files_in=$(grep -Ec 'neg_[0-9]{1,2}_in\.txt' "save_all.txt")
count_files_out=$(grep -Ec 'neg_[0-9]{1,2}_out\.txt' "save_all.txt")
if [ "$count_files_in" -eq "$count_files_out" ]; 
then
  if [ "$count_files_in" -ne 0 ]; 
  then
    for ((i=1; i < count_files_in + 1; i++ ))
    do
      if [ "$i" -lt 10 ];
      then
        data_in=$(cat "../data/neg_0${i}_in.txt")
        data_out=$(cat "../data/neg_0${i}_out.txt")
        bash neg_case.sh "$data_in" "$data_out"
        if [ $? -eq 1 ]; then
          rm save_all.txt
          echo "neg_0$i - ERROR"
          echo 1
          exit 1

        else
          echo "neg_0$i - OK"
        fi
        else
            data_in=$(cat "../data/neg_${i}_in.txt")
            data_out=$(cat "../data/neg_${i}_out.txt")
            bash neg_case.sh "$data_in $data_out"
          if [ $? -eq 1 ]; then
            rm save_all.txt
              echo "neg_$i - ERROR
              echo 1
              exit 1
              "
            else
              echo "neg_$i - OK"
          fi
    fi  
    done
  fi
else
  rm save_all.txt
  echo 1
  exit 1
fi
rm save_all.txt
echo 0
exit 0

