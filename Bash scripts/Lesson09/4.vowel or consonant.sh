#!/bin/bash

echo "This is script to check vovels and consonant: "

read -p "Enter the letter" WORD


WORD=$(echo "$WORD" | tr '[:upper:]' '[:lower:]')
case $WORD in
    a|e|i|o|u)
    echo "letter is vovel!"
    ;;
    b|c|d|f|g|h|j|k|l|m|n|p|q|r|s|t|v|w|x|y|z)
    echo "letter is consonant!"
esac    