#!/bin/sh

echo '''
import os
files = os.listdir()
summary = "\"id\",\"created\\_at\",\"name\",\"has\\_test\",\"alternate\\_url\"\\n"
for file in files:
    if file.endswith("\".csv"):
        with open(file) as handle:
            note = handle.readlines()
        summary += note[1]
with open("example.csv", "w") as handle2:
    handle2.write(summary.rstrip("\\n"))
''' > hw.py
python3 hw.py
rm hw.py
(cat example.csv | head -n 1; cat example.csv | tail -n +2 | sort -t ',' -k 2 -k 1)
rm example.csv