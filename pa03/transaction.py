'''
This app will have the following fields stored in a SQL table called transactions.
It will also allow the user to read and update the database as need.

'item #',
'amount',
'category',
'date',
'description'

@Author: Qiuyang Wang, Steve Wang
@Date: 2023-03-26
'''

import sqlite3
import os


def toDict(t):
    '''
    t is a tuple (itemID, amount, category, date, description)

    @Author: Qiuyang Wang
    '''
    transaction = {'itemID': t[0], 'amount': t[1],
                   'category': t[2], 'day': t[3], 'month': t[4], 'year': t[5], 'description': t[6]}
    return transaction


class Transaction():
    """
    @Author: Qiuyang Wang, Steve Wang
    """

    def __init__(self):
        self.runQuery('''CREATE TABLE IF NOT EXISTS transactions
                    (itemID text, amount int, category text, day int, month int, year int, description text)''', ())

    def runQuery(self, query, tuple):
        """
        @Author: Qiuyang Wang
        """
        con = sqlite3.connect('transactions.db')
        cur = con.cursor()
        cur.execute(query, tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [toDict(t) for t in tuples]

    def delete(self, itemID):
        """
        delete a transaction by a given itemID

        @Author: Qiuyang Wang
        """
        return self.runQuery("DELETE FROM transactions WHERE itemID=(?);", (itemID,))

    def show(self):
        '''
            returns all the transactions

            @Author: Steve Wang
        '''
        return self.runQuery("SELECT * FROM transactions;", ())

    def add(self, item):
        '''
            adds a transaction to the database

            @Author: Steve Wang
        '''
        dateLs = item['date'].split("/")
        if (len(dateLs) < 3):
            return "error"
        else:
            return self.runQuery("INSERT INTO transactions VALUES(?,?,?,?,?,?,?);", (item['itemID'], item['amount'], item['category'], int(dateLs[1]), int(dateLs[0]), int(dateLs[2]), item['description'],))

    def sumByDate(self):
        '''
            returns all the transactions grouped by day

            @Author: Quyang Wang
        '''
        return self.runQuery("SELECT * FROM transactions ORDER BY year, month, day ASC;", ())

    def sumByMonth(self, month):
        '''
            returns all the transactions grouped by month

            @Author: Steve Wang
        '''
        return self.runQuery("SELECT * FROM transactions WHERE month=(?);", (month,))

    def sumByYear(self, year):
        '''
            returns all the transactions grouped by year

            @Author: Steve Wang
        '''
        return self.runQuery("SELECT * FROM transactions WHERE year=(?);", (year,))

    def sumByCate(self, category):
        '''
            returns all the transactions grouped by category

            @Author: Steve Wang
        '''
        return self.runQuery("SELECT * FROM transactions WHERE category=(?);", (category,))
