#!/bin/bash

echo "This is FOR, WHILE loop counter:"

read -p "Enter the number to multiply: " X
read -p "Enter how many times to multiply it: " Y

#checking that x and y is numbers

if [[ "$X" =~  ^[0-9]+$ ]]
    then
    : #do nothing
    else
    echo "Invalid input. Only numbers are allowed."
    exit
fi

if
    [[ "$Y" =~ ^[0-9]+$ ]]
    then
    : #do nothing
    else
    echo "Invalid input. Only numbers are allowed."
    exit
 fi

#Multiplication table using FOR
echo "Multiplication table using FOR loop:"
for I in $(seq 1 $Y) #sequence from 1 to the number entered in Y
#seq is a command-line utility in Unix/Linux used to generate a sequence of numbers. It's often used in shell scripting for loops, especially when you want to loop over a specific numeric range.
#seq [start] [end]
#for i in $(seq 1 5)
#do
#  echo "Number: $i"
#dones
do
    echo "$X x $I = $((X * I))"
done

#Multiplication table using WHILE
echo "Multiplication table using WHILE loop:"
I=1 #Initializes counter
while [ $I -le $Y ] #Repeats the loop whil I is less than or equal to Y
do
    echo "$X x $I = $((X * I))" #Multipli
    ((I++))
done

