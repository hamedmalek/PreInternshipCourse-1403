#!/bin/bash


# A simple script to read user input and perform operations with them

echo -n "Enter number 1 : " # -n option supresses newline
read NUM1 # Read the user input from Standard Input and store in Variable NUM1

echo -n "Enter number 2 : "
read NUM2

SUM=$(($NUM1 + $NUM2)) # Arithmetic expansion using double parentheses
echo "The sum is $SUM"

SUM=`expr $NUM1 + $NUM2` # Arithmetic expansion using backticks. 
   #Usage of expr command to evaluate the expression
echo "The sum is $SUM"
