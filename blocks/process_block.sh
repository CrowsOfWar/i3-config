
bg_color="#FF0000"
fg_color="#000000"
var="$(python ~/.i3/blocks/$1.py)"
echo "<span foreground='$bg_color'>&#57522;</span><span background='$bg_color' foreground='$fg_color'> $var</span>"
#echo "<span foreground='$fg_color'>hello</span>"
