#!/bin/bash

# Description    : A script to show usage of if condition

#NUM1=5 # variable assignment
#NUM2=2

echo -n "enter number1: "
read num1
echo -n "enter number2: "
read num2

if [ $num1 -gt $num2 ] # -gt is to test integer numbers
then
    echo "num1 > num2"
else
    echo "num1 <= num2"	
fi
