#!/bin/bash

echo "This script is reading files in same file as folder and check word then outpoot lines that containes it"

read -p "enter file name.extension: " FILE
read -p "enter word or any symbols to search: " SYMBOL

#checking have writes to read and file to existance

if [[ -f "$FILE" && -r "$FILE" ]]; then
        echo "File exists and is readable."

    RESULT=$(grep "$SYMBOL" "$FILE") #checking if the result not 0:  != 0 not working
    if [[ -n "$RESULT" ]]; then
        echo "This is the result:"
        echo "$RESULT"
    else
        echo "Nothing found."
    fi

else
        echo "File does not exist or is not readable."
fi

#ask CHATGPT to comment
# read -p "Enter ...: " VARIABLE
# read - Reads input from the user.
# -p - Prompts the user with a custom message.
# VARIABLE - Stores the user input.

# -f "$FILE" - True if the file exists and is a regular file (not directory, socket, etc.).
# -r "$FILE" -True if the file is readable by the user running the script.
# && - Logical AND operator: both conditions must be true.
# then - Starts the code block that runs if the condition is true

# RESULT=$(grep "$SYMBOL" "$FILE") - Command substitution using $(...) – runs the command and stores the output in RESULT.

# grep - Searches for lines that contain the string in $SYMBOL.
# "...": - Double quotes allow variables and support spaces/special characters.

#if [[ -n "$RESULT" ]]; then - Checks if grep found something.
#-n "$RESULT" - True if the variable is not empty.
# echo "$RESULT" - Prints the actual lines that matched the search word or symbol.
# else ... fi - else: Code to run if the if condition is false.
# fi: Ends the if block.