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
    '''
    t is a tuple (item #, amount, category, date, description)
    
    @Author: Qiuyang Wang
    '''
    print('t='+str(t))
    transaction = {'item #':t[0], 'amount':t[1], 'category':t[2], 'date':t[3], 'description':t[4]}
    return transaction

class Transaction():
    """
    @Author: Qiuyang Wang
    """
    def __init__(self):
        self.runQuery('''CREATE TABLE IF NOT EXISTS transactions
                    (item # text, amount int, 'category text, date text, description text)''',())
    
    def runQuery(self,query,tuple):
        """
        @Author: Qiuyang Wang
        """
        con= sqlite3.connect('transactions.db')
        cur = con.cursor() 
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [toDict(t) for t in tuples]
    
