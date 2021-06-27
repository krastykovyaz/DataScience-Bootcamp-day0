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

counter_pos = {}
i = 0
try:
    for line in open("hh_positions.csv"):
        if i > 0:
            tmp_line = line.split(",")
            pos = str_contain(tmp_line[2])
            if pos in counter_pos:
                counter_pos[pos] += 1
            else:
                counter_pos[pos] = 1
        i += 1
except:
    print("Error is occurred")
    exit(1)
counter_pos = {k: v for k, v in sorted(counter_pos.items(), key=lambda item: item[1], reverse=True)}
summary = "\"name\",\"count\"" + "\\n"
for k, v in counter_pos.items():
    summary += str(k) + "," + str(v)
    summary += "\\n"
with open("hh_uniq_positions.csv", "w") as file:
  file.write(summary)
''' > hw.py
python3 hw.py
rm hw.py