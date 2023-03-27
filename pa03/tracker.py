#! /opt/miniconda3/bin/python3
'''
This program offers the user the following options and makes calls to the Transaction class to update the database.

@Author: Qiuyang Wang
@Date: 2023-03-22
'''

from transaction import Transaction
import sys


def print_usage():
    ''' 
    print an explanation of how to use this command 

    @Author: Qiuyang Wang
    '''
    print('''usage:
            tr quit
                expected argument: none
                example: tr quit
            tr show
                expected argument: none
                example: tr show
            tr add
                expected argument: item #, amount, category, date(in the form of MM/DD/YYYY), description, separated by space
                example: tr add 1 100 food "Some food"
            tr delete
                expected argument: item #
                example: tr delete 1
            tr summary_by_date
                expected argument: none
                example: tr summary_by_date
            tr summary_by_month
                expected argument: none
                example: tr summary_by_month
            tr summary_by_year
                expected argument: none
                example: tr summary_by_year
            tr summary_by_category
            tr print_menu
            '''
          )


def print_transactions(transactions):
    ''' 
    print the transactions in a nice format

    @Author: Qiuyang Wang
    '''
    if len(transactions) == 0:
        print('no transaction to print')
        return
    print('\n')
    print("%-10s %-10s %-10s %-10s %-30s" %
          ('item #', 'amount', 'category', 'date', 'description'))
    print('-'*40)
    for item in transactions:
        # (item #, amount, category, date, description)
        date = str(item['month'])+"/"+str(item['day'])+"/"+str(item['year'])
        values = (item['itemID'], item['amount'],
                  item['category'], date, item['description'])
        print("%-10s %10d %-10s %-10s %-30s" % values)


def process_args(args):
    '''
    examine args and make appropriate calls to Transaction

    @Author: Qiuyang Wang
    '''
    transaction = Transaction()
    if args == []:
        print_usage()
    elif args[0] == "quit":
        sys.exit()
    elif args[0] == "show":
        print_transactions(transaction.show())
    elif args[0] == "add":
        if len(args) != 6:
            print_usage()
        else:
            trans = {'itemID': args[1], 'amount': args[2],
                     'category': args[3], 'date': args[4], 'description': args[5]}
            rs = transaction.add(trans)
            if (rs == "error"):
                print_usage()
    elif args[0] == "delete":
        if len(args) != 1:
            print_usage()
        else:
            transaction.delete(args[1])
    elif args[0] == "summary_by_date":
        transaction.sumByDate()
    elif args[0] == "summary_by_month":
        transaction.sumByMonth(args[1])
    elif args[0] == "summary_by_year":
        transaction.sumByYear()
    elif args[0] == "summary_by_category":
        transaction.sumByCate(args[1])
    elif args[0] == "print_menu":
        print_usage()
    else:
        print(args, "is not implemented")
        print_usage()


def start():
    ''' 
    read the command args and process them

    @Author: Qiuyang Wang
    '''
    if len(sys.argv) == 1:
        # they didn't pass any arguments,
        # so prompt for them in a loop
        print_usage()
        args = []
        while args != ['']:
            args = input("command> ").split(' ')
            process_args(args)
            print('-'*40+'\n'*3)
    else:
        # read the args and process them
        args = sys.argv[1:]
        process_args(args)
        print('-'*40+'\n'*3)


start()
