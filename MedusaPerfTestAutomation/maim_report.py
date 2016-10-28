import csv
import os
import socket

filename = os.getcwd() + "/" + socket.gethostname() + ".csv"

with open(filename, 'r') as f:
    reader = csv.reader(f)
    tmp_t_result = []
    tmp_t_name = []
    tmp_t_field = []
    tmp_t_time = []

    for row in reader:

        if not row or row[0].startswith("--"):
            continue
        elif row[0] == "Sample Number":
            if not tmp_t_field:
                tmp_t_field.append(row)
                del tmp_t_field[0][0]
                tmp_t_field = tmp_t_field[0]
                tmp_t_field.insert(0, "Test Name")
                tmp_t_field.insert(1, "Start Time")

        elif "Command line" in row[0]:
            tmp_t_name.append(row[0].split("-f")[0].split("/")[-1])

        elif "Time" in row[0]:
            tmp_t_time.append(row[0].split(": ")[1])
        else:
            tmp_t_result.append(row[1:])

#for checking
#print len(tmp_t_name), tmp_t_name
#print len(tmp_t_field), tmp_t_field
#print len(tmp_t_time), tmp_t_time
#print len(tmp_t_result[0]), tmp_t_result
#print tmp_t_time
for i, j in enumerate(tmp_t_result):
    j.insert(0, tmp_t_name[i])
    j.insert(1, tmp_t_time[i])

# Create a file "Raw_Report.csv" with all the fields

with open('Raw_Report.csv', 'wb') as raw_csv:
    writer = csv.writer(raw_csv)
    writer.writerow(tmp_t_field)
    writer.writerows(tmp_t_result)

# Create the final file "Maim_Report.csv" with the specific fields
with open('Raw_Report.csv') as raw_csv:
    reader = csv.reader(raw_csv)
    col = [0, 1, 2, 4, 9, 12, 28]
    with open('Maim_Report.csv', 'wb') as maim_csv:
        writer = csv.writer(maim_csv)
        for row in reader:
            tmp = []
            for c in col:
                tmp.append(row[c])
            writer.writerow(tmp)
