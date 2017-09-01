import psutil
import math

mem = psutil.virtual_memory()
available_gb = int(mem.available / 1024.0 / 1024 / 1024)
total_gb = int(mem.total / 1024.0 / 1024 / 1024) + 1
pct = int(100.0 * mem.available / mem.total)

icon = "&#xf2db;"
message = str(available_gb) + '/' + str(total_gb) + ' gb (' + str(pct) + '%)'
print(icon + '   ' + message)

if pct < 30:
    print('i')

