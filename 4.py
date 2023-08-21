#Create salary.csv file which contain sid,sname,salary.
#Display the employee record whose name begins from "S‟ also show no. of employee with first letter "S‟ out of total record.
import csv
with open('salary.csv','w',newline='')as f:
    w.csv.writer(f)
    header=['sid','sname','salary']
    w.writerow(header)
    record=[[1,'om',4500],
           [2,'sai',4200],
           [3,'ram',5000],
           [4,'radha',5500],
           [5,'krishna',5700]]
w.writerows(record)
e=open('salary.csv','r')
f=csv.reader(e)
for i in f:
    print(i)
