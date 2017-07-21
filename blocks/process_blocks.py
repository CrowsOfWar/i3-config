
import subprocess

scripts = [ 'date', 'time', 'ram' ]
script_outputs = []
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
    if 'n' in flags:
        bg_color = '#2aa198'
        fg_color = '#073642'

    script_output = { 'bg_color': bg_color, 'fg_color': fg_color, 'output': output };
    script_outputs.append(script_output)

for i, script_output in enumerate(script_outputs):
    next_output = {}
    prev_output = script_output
    if i != 0:
        prev_output = script_outputs[i - 1]
    if i != (len(script_outputs) - 1):
        next_output = script_outputs[i + 1]

    formatting = { 'prev_bg': prev_output['bg_color'], 'bg': script_output['bg_color'], 'fg': script_output['fg_color'], 'output': script_output['output'] }
    total_output += "<span foreground='%(bg)s' background='%(prev_bg)s'>&#57522;</span><span background='%(bg)s' foreground='%(fg)s'> %(output)s </span>" % formatting

    #print('i%s %s %s' % (i, script_output, prev_output))

#total_output += "<span foreground='%(bg_color)s' background='%(fg_color)s'>&#57522;</span><span background='%(bg_color)s' foreground='%(fg_color)s'> %(output)s </span>" % script_output

print(total_output)
