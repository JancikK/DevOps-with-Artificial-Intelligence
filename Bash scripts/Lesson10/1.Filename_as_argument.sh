#!/bin/bash

check_permissions() { #function name
    local FILE="$1" #First argument. Keeps the file variable local to this function

    if [ -e "$FILE" ]; then #checks if the file exists
        echo "Checking permissions for: $FILE" #Prints which file we are checking.
        
        if [ -r "$FILE" ]; then #checks if the file is readable.
            echo "The file is readable."
        else
            echo "The file is NOT readable."
        fi

        if [ -w "$FILE" ]; then #checks if the file is writable.
            echo "The file is writable."
        else
            echo "The file is NOT writable."
        fi

        if [ -x "$FILE" ]; then #checks if the file is executable.
            echo "The file is executable."
        else
            echo "The file is NOT executable."
        fi
    else
        echo "The file does not exist." #prints a warning.
    fi
}

# Call the function with the first argument passed to the script
check_permissions "$1"