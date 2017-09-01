
import subprocess

scripts = [ 'date', 'time', 'ram' ]
script_outputs = []
total_output = ''

for script_name in scripts:
    result = subprocess.check_output('python ~/.i3/blocks/%s.py' % script_name, shell=True)
    result_split = result.split('\n')
    
    # Output of the block:
    #  line 1 - The text to display
    #  line 2 - flags (for coloring)

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
    prev_output = { 'bg_color': '#000000ff' }
    if i != 0:
        prev_output = script_outputs[i - 1]
    if i != (len(script_outputs) - 1):
        next_output = script_outputs[i + 1]
    
    # HTML attribute to use previous bg as background
    # However in first one, use a transparent (ie, no) background
    prev_bg_attr = "background='%s'" % prev_output['bg_color'] if i != 0 else ""

    # formatting values for "HTML", in python % notation
    formatting = { 'prev_bg': prev_output['bg_color'], 'bg': script_output['bg_color'], 'fg': script_output['fg_color'], 'output': script_output['output'], 'prev_bg_attr': prev_bg_attr }

    # arrow separating the 2 blocks
    arrow = "<span foreground='%(bg)s' %(prev_bg_attr)s>&#57522;</span>" % formatting
    # if the two blocks are same color, use an inverted arrow instead
    if prev_output['bg_color'] == script_output['bg_color']:
        arrow = "<span foreground='%(fg)s' background='%(bg)s'>&#57523;</span>" % formatting

    total_output += arrow + "<span background='%(bg)s' foreground='%(fg)s'> %(output)s </span>" % formatting

print(total_output)
