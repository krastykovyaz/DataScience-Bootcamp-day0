#!/bin/sh

#echo "\"id\", \"created_at\", \"name\", \"has_test\",\"alternate_url\"" > hh.csv
#jq -r '.items[] | [.id, .created_at, .name, .has_test, .alternate_url] | @csv' < hh.json |\
#sort --field-separator=',' --key=3 >> hh.csv
echo '''
full_file = ""
i = 0
try:
  for line in open("hh_positions.csv"):
    save_line = ""
    if i > 0:
      save_line += "\"id\",\"created\\_at\",\"name\",\"has\\_test\",\"alternate\\_url\"\\n"
      tmp_line = line.split(",")
      save_line += line
      with open(str(tmp_line[1]) + ".csv", "w") as file:
          file.write(save_line)
      line = ",".join(tmp_line)
    full_file += line
    i += 1
except:
  print("Error is occurred")
  exit(1)
''' > hw.py
python3 hw.py
rm hw.py