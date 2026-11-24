import csv, statistics
from pathlib import Path

rows = list(csv.DictReader(Path('data.csv').open()))
vals = [int(r['value']) for r in rows]
print('n', len(vals), 'mean', round(statistics.mean(vals), 2), 'max', max(vals))
