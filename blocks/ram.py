import psutil
import math

mem = psutil.virtual_memory()
available_gb = round(mem.available / 1024.0 / 1024 / 1024, 1)
total_gb = round(mem.total / 1024.0 / 1024 / 1024, 1)
pct = round(available_gb / total_gb * 100, 1)

print('Memory: ' + str(available_gb) + '/' + str(total_gb) + ' gb (' + str(pct) + '%) available')

