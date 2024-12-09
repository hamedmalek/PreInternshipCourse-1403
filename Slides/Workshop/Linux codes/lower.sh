#!/bin/bash

# Description    : A script to show usage of if else condition

echo -n "enter NUM1: "
read NUM1
echo -n "enter NUM2: "
read NUM2


if [ $NUM1 -lt $NUM2 ]  # -lt is to test integer numbers
then
    echo "NUM1 < NUM2"
elif [ $NUM1 -eq $NUM2 ]
then
    echo "NUM1 = NUM2"
else
    echo "NUM1 > NUM2"
fi
