#!/bin/bash

for ((i=-10; i<=10; i+=2))
do
    for ((j=-35; j<=35; j+=1))
    do
        ((x=i*2))
        ((y=j*4))
        ((a=x*x+y*y-400))
        ((b=(x-10)*(x-10)+y*y-400))
        ((c=(x+10)*(x+10)+y*y-400))
        ((d=x*x+(y-10)*(y-10)-400))
        ((e=x*x+(y+10)*(y+10)-400))
        ((f=a*b*c*d*e))
        if [ $f -le 0 ]; then
            echo -n "*"
        else
            echo -n " "
        fi
    done
    echo ""
done

#run in your bash 

bash donut.sh

# This script uses nested loops to iterate through the characters in the terminal and uses a mathematical expression to determine whether to print an asterisk (*) or a space ( ) to form the donut shape.
