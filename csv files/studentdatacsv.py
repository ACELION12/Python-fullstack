import csv
with open("/Users/sathwikkumar/Python full stack /csv files/student_data.csv") as file1:
    content=csv.reader(file1)
    for row in content:
        print(row)