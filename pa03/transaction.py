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


def to_dict(t):
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
        self.run_query('''CREATE TABLE IF NOT EXISTS transactions
                    (itemID text, amount int, category text, day int, 
                    month int, year int, description text)''', ())

    def run_query(self, query, tpl):
        """
        @Author: Qiuyang Wang
        """
        con = sqlite3.connect('transactions.db')
        cur = con.cursor()
        cur.execute(query, tpl)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [to_dict(t) for t in tuples]

    def delete(self, item_id):
        """
        delete a transaction by a given itemID

        @Author: Qiuyang Wang
        """
        return self.run_query("DELETE FROM transactions WHERE itemID=(?);", (item_id,))

    def show(self):
        '''
            returns all the transactions

            @Author: Steve Wang
        '''
        return self.run_query("SELECT * FROM transactions;", ())

    def add(self, item):
        '''
            adds a transaction to the database

            @Author: Steve Wang
        '''
        date_ls = item['date'].split("/")
        if len(date_ls) < 3:
            return "error"
        return self.run_query("INSERT INTO transactions VALUES(?,?,?,?,?,?,?);",
                              (item['itemID'],
                               item['amount'],
                               item['category'],
                               int(date_ls[1]),
                               int(date_ls[0]),
                               int(date_ls[2]),
                               item['description'],
                               ))

    def sum_by_date(self):
        '''
            returns all the transactions grouped by day

            @Author: Quyang Wang
        '''
        return self.run_query("SELECT * FROM transactions ORDER BY year, month, day ASC;", ())

    def sum_by_month(self, month):
        '''
            returns all the transactions grouped by month

            @Author: Steve Wang
        '''
        return self.run_query("SELECT * FROM transactions WHERE month=(?);", (month,))

    def sum_by_year(self, year):
        '''
            returns all the transactions grouped by year

            @Author: Steve Wang
        '''
        return self.run_query("SELECT * FROM transactions WHERE year=(?);", (year,))

    def sum_by_cate(self, category):
        '''
            returns all the transactions grouped by category

            @Author: Steve Wang
        '''
        return self.run_query("SELECT * FROM transactions WHERE category=(?);", (category,))
