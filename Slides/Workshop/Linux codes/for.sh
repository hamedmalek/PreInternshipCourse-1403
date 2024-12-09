#!/bin/bash

# Sum of N natural numbers using for loop

echo -n "Enter a Number: "
read NUM

SUM=0

for I in `seq $NUM`  # seq command provides a sequence of numbers from 0 to $NUM
do
    SUM=`expr $SUM + $I`
    let I+=1
done

echo "The sum of the first $NUM numbers is: $SUM"
