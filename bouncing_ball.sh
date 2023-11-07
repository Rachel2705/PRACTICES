#!/bin/bash

tput civis # Hide the cursor
trap 'tput cnorm; exit' INT TERM # Restore cursor visibility and exit on interrupt

while true; do
    for i in {1..20}; do
        clear
        printf "\033[%d;%dH●\n" $i 10
        sleep 0.05
    done

    for i in {19..2}; do
        clear
        printf "\033[%d;%dH●\n" $i 10
        sleep 0.05
    done
done

# run bash 
bash bouncing_ball.sh

