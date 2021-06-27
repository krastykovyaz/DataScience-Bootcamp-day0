#!/bin/sh

echo '''
def str_contain(x):
  x = str(x).lower()
  status = ""
  if "senior" in x:
    status += "Senior/"
  if "middle" in x:
    status += "Middle/"
  if "junior" in x:
    status += "Junior/"
  if "junior" not in x and "middle" not in x and "senior" not in x:
    status += "-"
  return "\"" + status.rstrip("/") + "\""

full_file = ""
i = 0
try:
  for line in open("hh_sorted.csv"):
    if i > 0:
      tmp_line = line.split(",")
      tmp_line[2] = str_contain(tmp_line[2])
      line = ",".join(tmp_line)
    full_file += line
    i += 1
except:
  print("Error is occurred")
  exit(1)
with open("hh_positions.csv", "w") as file:
  file.write(full_file)
''' > hw.py
python3 hw.py
rm hw.py