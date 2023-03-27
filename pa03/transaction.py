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
    t is a tuple (itemID, amount, category, date, description)

    @Author: Qiuyang Wang
    '''
    transaction = {'itemID': t[0], 'amount': t[1],
                   'category': t[2], 'day': t[3], 'month': t[4], 'year': t[5], 'description': t[6]}
    return transaction


class Transaction():
    """
    @Author: Qiuyang Wang
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
        # s = ""
        # q = self.runQuery("SELECT * FROM transactions", ())
        # for entry in q:
        #     date = entry['month']+entry['date']+entry['year']
        #     s += entry['itemID'] + "\t" + entry['amount']+"\t" + \
        #         entry['category']+"\t"+date+"\t"+entry['description']+"\n"
        # print_prompt(s)
        return self.runQuery("SELECT * FROM transactions;", ())

    def add(self, item):
        dateLs = item['date'].split("/")
        if (len(dateLs) < 3):
            return "error"
        else:
            return self.runQuery("INSERT INTO transactions VALUES(?,?,?,?,?,?,?);", (item['itemID'], item['amount'], item['category'], int(dateLs[1]), int(dateLs[0]), int(dateLs[2]), item['description'],))

    def sumByDate(self):
        # q = self.show()

        return self.runQuery("SELECT * FROM transactions ORDER BY year, month, day ASC;", ())
        # returnQ = []
        # for entry in q:
        #     if (entry['date'][2:4] == date):
        #         returnQ.append(entry)
        # return returnQ

    def sumByMonth(self, month):
        # q = self.runQuery(
        #     "SELECT item #, amount, category, description FROM transactions where date=(?)", (date,))
        # q = self.show()
        # print(q[0])
        # returnQ = []
        # for entry in q:
        #     if (entry['date'][:2] == month):
        #         returnQ.append(entry)
        # return returnQ
        return self.runQuery("SELECT * FROM transactions WHERE month=(?);", (month,))

    def sumByYear(self, year):
        # q = self.runQuery(
        #     "SELECT item #, amount, category, description FROM transactions where date=(?)", (date,))
        # q = self.show()
        # returnQ = []
        # for entry in q:
        #     if (entry['date'][4:] == year):
        #         returnQ.append(entry)
        # return returnQ
        return self.runQuery("SELECT * FROM transactions WHERE year=(?);", (year,))

    def sumByCate(self, category):
        return self.runQuery("SELECT * FROM transactions WHERE category=(?);", (category,))
