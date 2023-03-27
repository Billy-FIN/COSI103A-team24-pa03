#! /opt/miniconda3/bin/python3
'''
This program offers the user the following options and makes 
calls to the Transaction class to update the database.

@Author: Qiuyang Wang, Steve Wang
@Date: 2023-03-26
'''

import sys
from transaction import Transaction


def print_usage():
    '''
    print an explanation of how to use this command

    @Author: Qiuyang Wang
    '''
    print('''usage:
            tr quit
                expected argument: none
                example: quit
            tr show
                expected argument: none
                example: tr show
            tr add
                #, amount, category, date(in the form of MM/DD/YYYY), description, separated by space
                expected argument: item
                example: tr add 1 100 food 1/1/2022 "Some food"
            tr delete
                expected argument: item #
                example: tr delete 1
            tr summary_by_date
                expected argument: none
                example: tr summary_by_date
            tr summary_by_month
                expected argument: 11
                example: tr summary_by_month 11
            tr summary_by_year
                expected argument: year
                example: tr summary_by_year 2023
            tr summary_by_category
                expected argument: category
                example: tr summary_by_category food
            tr print_menu
                expected argument: none
                example: tr print_menu
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
    # print("%-10s %-10s %-10s %-10s %-30s" %
    #       ('item #', 'amount', 'category', 'date', 'description'))
    print(f"{'item #'}\t\t{'amount'}\t\t{'category'}\t{'date'}\t\t{'description'}\t")
    print('-'*80)
    for item in transactions:
        # (item #, amount, category, date, description)
        date = str(item['month'])+"/"+str(item['day'])+"/"+str(item['year'])
        values = (item['itemID'], item['amount'],
                  item['category'], date, item['description'])
        print(
            f"{values[0]}\t\t{values[1]}\t\t{values[2]}\t\t{values[3]}\t{values[4]}\t")


def process_args(args):
    '''
    examine args and make appropriate calls to Transaction

    @Author: Qiuyang Wang, Steve Wang
    '''
    transaction = Transaction()
    if args == []:
        print_usage()
    elif args[0] == "quit" and len(args) == 1:
        sys.exit()
    elif len(args) == 1:
        print("Please follow the format!")
        print_usage()
    elif args[1] == "show":
        print_transactions(transaction.show())
    elif args[1] == "add":
        if len(args) <= 7:
            print_usage()
        else:
            desc = ""
            for i in range(6, len(args)):
                desc += args[i] + " "
            trans = {'itemID': args[2], 'amount': args[3],
                     'category': args[4], 'date': args[5], 'description': desc.rstrip()}
            res = transaction.add(trans)
            if res == "error":
                print("Please follow the format!")
                print_usage()
    elif args[1] == "delete":
        if len(args) != 3:
            print("Please follow the format!")
            print_usage()
        else:
            transaction.delete(args[2])
    elif args[1] == "summary_by_date":
        print_transactions(transaction.sum_by_date())
    elif args[1] == "summary_by_month":
        print_transactions(transaction.sum_by_month(args[2]))
    elif args[1] == "summary_by_year":
        print_transactions(transaction.sum_by_year(args[2]))
    elif args[1] == "summary_by_category":
        print_transactions(transaction.sum_by_cate(args[2]))
    elif args[1] == "print_menu":
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
