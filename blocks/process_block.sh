#!/bin/bash

bg_color="#073642"
fg_color="#839496"
output="$(python ~/.i3/blocks/$1.py)"

if [[ $output == i* ]] ;
then
    bg_color="#d33682"
    fg_color="#073642"
    output=${output:1}
fi

formatted="<span foreground='$bg_color' background='$fg_color'>&#57522;</span><span background='$bg_color' foreground='$fg_color'> $output </span>"

echo $formatted
