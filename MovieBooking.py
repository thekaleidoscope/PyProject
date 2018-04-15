#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('movies.db')
print('Connected successful to the database')

moviec=3
conn.execute(''' CREATE TABLE IF NOT EXISTS Movies(id int primary key, moviename text not null,Seats int ,price int);''')
print('\nMovie Theater Active')


def newmovie(_id,mname,tseats,_price):
        #print(' Insert Into Movies(id,moviename, Seats,price) Values({:d},"{}",{:d},{:d});'.format(_id,mname,tseats,_price))
    conn.execute(' Insert Into Movies(id,moviename, Seats,price) Values({},"{}",{},{});'.format(_id,mname,tseats,_price))

def showmoviesall():
    print('\nAll Movies Played')

    cursor= conn.execute(''' Select id,moviename, Seats,price From Movies ''')
    for row in cursor:
        print('Movie Id:', row[0])
        print('Movie Name:', row[1])
        print('Seats Available', row[2])
        print('Ticket Price:', row[3])


def showmovie(id):
    cursor= conn.execute(''' Select id,moviename, Seats,price From Movies where id is {} '''.format(id))
    print("\nMovie chosen is {}".format(cursor.fetchone()[1]))
    cursor= conn.execute(''' Select id,moviename, Seats,price From Movies where id is {} '''.format(id))
    for row in cursor:
        print('Movie Id:', row[0])
        print('Movie Name:', row[1])
        print('Seats Available', row[2])
        print('Ticket Price:', row[3])
def fetchseat(id):
    cursor= conn.execute(''' Select Seats From Movies where id is {} '''.format(id))
    return(cursor.fetchone()[0])

def fetchmovie(id):
    cursor= conn.execute(''' Select moviename From Movies where id is {} '''.format(id))
    return(cursor.fetchone()[0])

def book(id,seat):
    conn.execute('''Update Movies Set Seats ={} where id is {}; '''.format(fetchseat(id)-seat,id))

def refundseat(id,seat):
    conn.execute('''Update Movies Set Seats ={} where id is {}; '''.format(fetchseat(id)+seat,id))

def removemovie(id):
    conn.execute('''Delete From Movies Where id is {} '''.format(id))
    
if __name__== '__main__':


    movies = [
        (1,"The Hunger Games: Catching Fire", 100,120),
        (2,"Wreck-It Ralph", 70,100),
        (3,"Her", 80,122)
        ]

    conn.executemany(""" INSERT INTO Movies(
    movie_name, movie_rating) VALUES(?,?)
    """, movies)
    conn.commit()
