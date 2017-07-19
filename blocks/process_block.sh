#!/bin/bash

bg_color="#073642"
fg_color="#839496"
output="$(python ~/.i3/blocks/$1.py)"

formatted="<span foreground='$bg_color'>&#57522;</span><span background='$bg_color' foreground='$fg_color'> $output </span>"

if [[ $output == i* ]] ;
then
    formatted="important"
fi

echo $formatted
