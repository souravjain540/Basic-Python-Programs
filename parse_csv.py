import csv
#read from csv
fields=list()
rows=list()
with open('employee.csv','r') as csv_file:
    csv_reader=csv.reader(csv_file)
    fields=next(csv_reader) #csv reader object
    for row in csv_reader:
        rows.append(row)
    print("Total no. of rows={}".format(csv_reader.line_num))
print("Field Names are:"+",".join(field for field in fields))
print("First 5 rows are:\n")
for row in rows[:5]:
    for col in row:
        print("{}".format(col),end=" "),
    print("\n")
#write to csv
flds=['Name','Branch','Year','CGPA']
rw= [['Nikhil', 'COE', '2', '9.0'],
        ['Sanchit', 'COE', '2', '9.1'],
        ['Aditya', 'IT', '2', '9.3'],
        ['Sagar', 'SE', '1', '9.5'],
        ['Prateek', 'MCE', '3', '7.8'],
        ['Sahil', 'EP', '2', '9.1']]
with open("university.csv",'w') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(flds)
    csvwriter.writerows(rw)
#write dictionary to csv

mydict =[{'branch': 'COE', 'cgpa': '9.0',
          'name': 'Nikhil', 'year': '2'},
        {'branch': 'COE', 'cgpa': '9.1',
         'name': 'Sanchit', 'year': '2'},
        {'branch': 'IT', 'cgpa': '9.3',
         'name': 'Aditya', 'year': '2'},
        {'branch': 'SE', 'cgpa': '9.5',
         'name': 'Sagar', 'year': '1'},
        {'branch': 'MCE', 'cgpa': '7.8',
         'name': 'Prateek', 'year': '3'},
        {'branch': 'EP', 'cgpa': '9.1',
         'name': 'Sahil', 'year': '2'}]

with open("college.csv",'w',newline='') as cv:
    fieldnames=["branch","cgpa","name","year"]
    writer=csv.DictWriter(cv,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(mydict)
with open("college.csv",'r') as cvf:
    reader=csv.DictReader(cvf)
    for row in reader:
        print(row['name'],row['branch'])   