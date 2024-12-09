#!/bin/bash

#A simple script to print the calender month

echo "The Month is: "
cal

echo "An alternative view of calender: "
date | awk '{print $2}'
