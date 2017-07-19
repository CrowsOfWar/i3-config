
bg_color="#073642"
fg_color="#839496"
var="$(python ~/.i3/blocks/$1.py)"
echo "<span foreground='$bg_color'>&#57522;</span><span background='$bg_color' foreground='$fg_color'> $var </span>"
#echo "<span foreground='$fg_color'>hello</span>"
