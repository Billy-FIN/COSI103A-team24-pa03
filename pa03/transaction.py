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
    transaction = {'item': t[0], 'amount': t[1],
                   'category': t[2], 'date': t[3], 'description': t[4]}
    return transaction


class Transaction():
    """
    @Author: Qiuyang Wang
    """

    def __init__(self):
        self.runQuery('''CREATE TABLE IF NOT EXISTS transactions
                    (item text, amount int, category text, date text, description text)''', ())

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
        delete a transaction by a given item #

        @Author: Qiuyang Wang
        """
        return self.runQuery("DELETE FROM transactions WHERE item=(?)", (itemID,))

    def show(self):
        return self.runQuery("SELECT * FROM transactions", ())

    def add(self, item):
        return self.runQuery("INSERT INTO transactions VALUES(?,?,?,?,?)", (item['item'], item['amount'], item['category'], item['date'], item['description'],))

    def sumByDate(self, date):
        q = self.show()
        # q = self.runQuery("SELECT item #, amount, category, description FROM transactions where date=(?)", (date,))
        returnQ = []
        for entry in q:
            if (entry['date'][:2] == date):
                returnQ.append(entry)
        return returnQ

    def sumByMonth(self, month):
        # q = self.runQuery(
        #     "SELECT item #, amount, category, description FROM transactions where date=(?)", (date,))
        q = self.show()
        returnQ = []
        for entry in q:
            if (entry['date'][2:4] == month):
                returnQ.append(entry)
        return returnQ

    def sumByYear(self, year):
        # q = self.runQuery(
        #     "SELECT item #, amount, category, description FROM transactions where date=(?)", (date,))
        q = self.show()
        returnQ = []
        for entry in q:
            if (entry['date'][4:] == year):
                returnQ.append(entry)
        return returnQ

    def sumByCate(self, category):
        return self.runQuery("SELECT item, amount, date, description FROM transactions where category=(?)", (category,))
