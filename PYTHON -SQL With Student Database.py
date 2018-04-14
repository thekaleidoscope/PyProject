#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('Student.db') 
print('Connected successful to the database')

conn.execute(''' Drop Table Student;''')
conn.execute(''' Create Table Student(regno text not null, name text not null, dob text not null, avg_marks int, status text, dept text);''')
print('\nTable Created Successfully')

conn.execute(''' Insert Into Student(regno, name, dob, avg_marks, status, dept) Values(537, 'Rachit', '25 December 1996', 95, '', 'CSE');''')

conn.execute(''' Insert Into Student(regno, name, dob, avg_marks, status, dept) Values(500, 'Raghav', '12 January 1996', 45, '', 'CSE');''')

conn.execute(''' Insert Into Student(regno, name, dob, avg_marks, status, dept) Values(538, 'Emma', '10 July 1997', 80, '', 'IT');''')

print('\nRecords added successfully')

cursor= conn.execute(''' Select regno, name, dob, avg_marks, status, dept From Student ''')
for row in cursor:
    print('Regno=', row[0])
    print('Name=', row[1])
    print('Date of Birth=', row[2])
    print('Avg_Marks=', row[3])
    print('Status=', row[4])
    print('Dept=', row[5], '\n')

cursor1= conn.execute(''' Select regno, name, dob, avg_marks, status, dept From Student; ''')
print('\nFetching all the data')
rows=cursor1.fetchall()
for ele in rows:
    print(ele)

cursor2= conn.execute(''' Select regno, name, dob, avg_marks, status, dept From Student where regno='537'; ''')
print('\nFetching data based on regno=537')
rows=cursor2.fetchall()
for ele in rows:
    print(ele)

cursor3= conn.execute(''' Select regno, name, dob, avg_marks, status, dept From Student where dept='CSE'; ''')
print('\nFetching data based on dept=CSE')
rows=cursor3.fetchall()
for ele in rows:
    print(ele)

cursor4= conn.execute(''' Select regno, name, dob, avg_marks, status, dept From Student; ''')
print('\nBefore Updation')
rows=cursor4.fetchall()
for ele in rows:
    print(ele)

conn.execute('''Update Student Set status ='Pass' where avg_marks>=50; ''')
conn.execute('''Update Student Set status ='Fail' where avg_marks<50; ''')

print('\nAfter Updation')
cursor5= conn.execute(''' Select * From Student; ''')

rows=cursor5.fetchall()
for ele in rows:
    print(ele)


conn.execute('''Delete From Student Where dept='IT' ''')

print('\nAfter Deletion')
cursor7= conn.execute(''' Select * From Student ''')

rows=cursor7.fetchall()
for ele in rows:
    print(ele)

print('Using Fetchone')
data=('CSE',)
c=conn.cursor()
c.execute(''' Select * From Student where dept=?''', data)
print(c.fetchone())

print('Using executemany()')
data = [('217', 'Emma', '4 October 1996 ', 99, 'Pass', 'IT'),
('180', 'Raghu', '30 December 1996 ', 95, 'Pass', 'CSE')]

c.executemany('Insert into Student Values(?,?,?,?,?,?)', data)
c.execute(''' Select * From Student ''')
print(c.fetchall())
#a=sqlite3_total_changes()
#print(a)
conn.commit()
conn.close()
print('\nAll Operations successful')
