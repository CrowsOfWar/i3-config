
import subprocess

scripts = [ 'date', 'time', 'ram' ]
total_output = ''

for script_name in scripts:
    result = subprocess.check_output('python ~/.i3/blocks/%s.py' % script_name, shell=True)
    result_split = result.split('\n')

    output = result_split[0]
    flags = '' if len(result_split) < 2 else result_split[1]

    bg_color = '#073642';
    fg_color = '#839496';

    if 'i' in flags:
        bg_color = '#d33682'
        fg_color = '#073642'

    total_output += "<span foreground='%(bg_color)s' background='%(fg_color)s'>&#57522;</span><span background='%(bg_color)s' foreground='%(fg_color)s'> %(output)s </span>" % { 'bg_color': bg_color, 'fg_color': fg_color, 'output': output }

print(total_output)
