
import subprocess

scripts = [ 'date', 'time', 'ram' ]

for script_name in scripts:
    result = subprocess.check_output('python %s.py' % script_name, shell=True)
    result_split = result.split('\n')
    print('Ran %s.py, got %s' % (script_name, result))
