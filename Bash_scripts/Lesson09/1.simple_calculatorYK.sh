#!/bin/bash

echo "This is simple calculator:"

read -p "Enter first number: " X
read -p "Enter second number: " Y

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

#asking user to enter operator
 read -p "Enter operator (+, -, *, /): " OP
if [[ "$OP" =~ ^[\+\-\*/\]$ ]]
    then
    : #do nothing
    else
    echo "Enter correct operator!"
    exit
 fi

#calculating part
if [ "$OP" = "+" ]
    then 
let SUM=X+Y 
echo "Result is: " $SUM
fi

if [ "$OP" = "-" ]
    then 
let SUM=X-Y 
echo "Result is: " $SUM
fi

if [ "$OP" = "*" ]
    then 
let SUM=X*Y 
echo "Result is: " $SUM
fi

if [ "$OP" = "/" ] 
then
    if [ "$Y" -eq 0 ]
     then
        echo "Can't divide by 0"
    else
        let SUM=X/Y
        echo "Result is: $SUM"
    fi
fi
