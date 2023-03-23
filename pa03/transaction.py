'''
This app will have the following fields stored in a SQL table called transactions.
It will also allow the user to read and update the database as need.

'item #',
'amount',
'category',
'date',
'description'

@Author: Qiuyang Wang
@Date: 2023-03-22
'''

import sqlite3
import os

def toDict(t):
    ''' t is a tuple (item #, amount, category, date, description)'''
    print('t='+str(t))
    todo = {'rowid':t[0], 'title':t[1], 'desc':t[2], 'completed':t[3]}
    return todo

class Transaction():
    def __init__(self):
        self.runQuery('''CREATE TABLE IF NOT EXISTS transactions
                    ('item #', 'amount', 'category', 'date', 'description')''',())
    
    def runQuery(self,query,tuple):
        con= sqlite3.connect('transactions.db')
        cur = con.cursor() 
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [toDict(t) for t in tuples]