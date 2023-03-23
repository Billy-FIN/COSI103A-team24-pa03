#! /opt/miniconda3/bin/python3
'''
This program offers the user the following options and makes calls to the Transaction class to update the database.

@Author: Qiuyang Wang
@Date: 2023-03-22
'''

from transaction import Transaction
import sys

# here are some helper functions ...

def print_usage():
    ''' print an explanation of how to use this command '''
    print('''usage:
            
            '''
            )

def print_todos(transactions):
    ''' print the todo items '''
    if len(transactions)==0:
        print('no tasks to print')
        return
    print('\n')
    print("%-10s %-10s %-30s %-10s"%('item #','title','desc','completed'))
    print('-'*40)
    for item in transactions:
        values = tuple(item.values()) #(item #, amount, category, date, description)
        print("%-10s %-10s %-30s %2d"%values)

def process_args(args):
    return

def toplevel():
    ''' read the command args and process them'''
    if len(sys.argv)==1:
        # they didn't pass any arguments, 
        # so prompt for them in a loop
        print_usage()
        args = []
        while args!=['']:
            args = input("command> ").split(' ')
            if args[0]=='add':
                # join everyting after the name as a string
                args = ['add',args[1]," ".join(args[2:])]
            process_args(args)
            print('-'*40+'\n'*3)
    else:
        # read the args and process them
        args = sys.argv[1:]
        process_args(args)
        print('-'*40+'\n'*3)

    

toplevel()