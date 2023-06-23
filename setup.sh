#!/bin/bash

green="\033[32m"
red="\033[91m"
orange="\033[93m"
blue="\033[96m"
reset="\033[0m"

steps_success=0
steps_total=4

echo "    QR Code Generator - Setup"
echo -e "${blue}[-]${reset} Python installed."
steps_success=$(($steps_success + 1))
python3 -m ensurepip --upgrade
echo -e "${blue}[-]${reset} Pip installed."
steps_success=$(($steps_success + 1))
# create virtual environment
python3 -m venv .venv
if [ -f ".venv" ]; then
    echo -e "${green}[-]${reset} Virtual environment created."
    steps_success=$(($steps_success + 1))
else
    echo -e "${red}[!]${reset} ERROR while creating virtual environment."
fi
# activate virtual environment
source .venv/bin/activate
if [ -z "$(env | grep )" ]; then
    echo -e "${red}[!]${reset} ERROR virtual env could not be activated."
else
    echo -e "${green}[-]${reset} Virtual env activated."
    steps_success=$(($steps_success + 1))
fi
echo -e "    SUMMARY: ${blue}${steps_success}${reset} / ${steps_total} successful."
