#!/bin/bash

# color codes
green="\033[32m"
red="\033[91m"
orange="\033[93m"
blue="\033[96m"
reset="\033[0m"

# important variables
venv_created=0
venv_activated=0
steps_success=0
steps_total=5

echo "    QR Code Generator - Setup"
# assume Python is installed by default on all Linux and MacOS systems
echo -e "${blue}[-]${reset} Python installed."
steps_success=$(($steps_success + 1))
# if Python is installed, then ensurepip will install Pip if necessary
python3 -m ensurepip --upgrade
echo -e "${blue}[-]${reset} Pip installed."
steps_success=$(($steps_success + 1))

# check if virtual environment already exists
if [[ -d ".venv" ]]; then
    echo -e "${green}[-]${reset} Virtual environment already exists."
    steps_success=$(($steps_success + 1))
    venv_created=1
else
    # create virtual environment
    python3 -m venv .venv
    if [[ -d ".venv" ]]; then
        echo -e "${green}[-]${reset} Virtual environment created."
        steps_success=$(($steps_success + 1))
        venv_created=1
    else
        echo -e "${red}[!]${reset} ERROR while creating virtual environment."
    fi
fi

# check if a virtual environment is already active
if [[ -v "VIRTUAL_ENV" ]]; then
    echo -e "${green}[-]${reset} Virtual env is already active."
            steps_success=$(($steps_success + 1))
            venv_activated=1
else
    # activate virtual environment
    if [[ $venv_created -eq 1 ]]; then
        source .venv/bin/activate
        if [[ -v "VIRTUAL_ENV" ]]; then
            echo -e "${red}[!]${reset} ERROR virtual env could not be activated."
        else
            echo -e "${green}[-]${reset} Virtual env activated."
            steps_success=$(($steps_success + 1))
            venv_activated=1
        fi
    fi
fi

# install dependencies
if [[ $venv_activated -eq 1 ]]; then
    python3 -m pip install -q -r requirements.txt
    echo -e "${green}[-]${reset} Dependencies installed"
    steps_success=$(($steps_success + 1))
fi

# print summary
if [[ $steps_success -eq 5 ]]; then
    echo -e "    SUMMARY: ${green}${steps_success}${reset} / ${steps_total} successful."
elif [[ $steps_success -gt 2 ]]; then
    echo -e "    SUMMARY: ${orange}${steps_success}${reset} / ${steps_total} successful."
else
    echo -e "    SUMMARY: ${red}${steps_success}${reset} / ${steps_total} successful."
fi
