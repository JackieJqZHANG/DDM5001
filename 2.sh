#!/bin/bash
i=0
sum=0
mkdir 5001
while (( i <= 100 ))
do
    cd
    mkdir 5001/DDM${i}
    cd 5001/DDM${i}    
    echo "<"`date +%s%N`">" >time_till_now.txt
    ((sum += i))
    ((i++))
done
#echo ${sum}