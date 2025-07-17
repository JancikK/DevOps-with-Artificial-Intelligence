#!/bin/bash

CREATEFOLDER () {
    mkdir -p "$1"
}


CREATEFILE () {
    touch "$1/$2"
}

read -p "Enter name of folder: " FLNAME
read -p "Enter file name: " FILNAME





