#!/bin/bash

UPPERCASE () {
    local INPUT=$1
    echo "${INPUT^^}"
}
read -p "Type text to convert: " TEXT

if [[ $TEXT =~ ^[A-Za-z]+$ ]]
    then
    RESULT=$(UPPERCASE "TEXT")
    echo "There is your UPPERCASE text: " $RESULT
    else
    echo "Only text input correct"
fi

