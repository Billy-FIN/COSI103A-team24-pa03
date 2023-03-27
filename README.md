# cosi103a-team24-pa03
This is a git repository which contains the code of programming assignment 03 (pa03) for cosi103a in Brandeis University.

## Collaborators:
 - Steve Wang ([Yell0wF1sh/github.com](https://github.com/Yell0wF1sh))
 - Qiuyang Wang https://github.com/Billy-FIN
 - Shentong Rao https://github.com/Shentongr

## Transcript:
PS F:\Qiongyue\study\Brandeis University\Spring 2023\CS 103A\cosi103a-team24-pa03>  & 'C:\Users\穹月\AppData\Local\Programs\Python\Python311\python.exe' 'c:\Users\穹月\.vscode\extensions\ms-python.python-2023.4.1\pythonFiles\lib\python\debugpy\adapter/../..\debugpy\launcher' '52830' '--' 'f:\Qiongyue\study\Brandeis University\Spring 2023\CS 103A\cosi103a-team24-pa03\pa03\tracker.py'
usage:
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

command> tr show


item #     amount     category   date       description
------------------------------------------------------------
2          100        mood       3/27/2023            'da'
12         100        food       11/11/2022           "Some food"
2          100        food       1/11/2022            "Some food"
1          100        food       1/1/2022             "Some food"
----------------------------------------



command> tr add 3 10000 tuition 1/1/2023 "brandeis tuition" 
----------------------------------------



command> tr show


item #     amount     category   date       description
------------------------------------------------------------
2          100        mood       3/27/2023            'da'
12         100        food       11/11/2022           "Some food"
2          100        food       1/11/2022            "Some food"
1          100        food       1/1/2022             "Some food"
3          10000      tuition    1/1/2023             "brandeis tuition"
----------------------------------------



command> tr delete 12
----------------------------------------



command> tr show


item #     amount     category   date       description
------------------------------------------------------------
2          100        mood       3/27/2023            'da'
2          100        food       1/11/2022            "Some food"
1          100        food       1/1/2022             "Some food"
3          10000      tuition    1/1/2023             "brandeis tuition"
----------------------------------------



command> tr print_menu
usage:
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

----------------------------------------



command> tr summary_by_date


item #     amount     category   date       description
------------------------------------------------------------
1          100        food       1/1/2022             "Some food"
2          100        food       1/11/2022            "Some food"
3          10000      tuition    1/1/2023             "brandeis tuition"
2          100        mood       3/27/2023            'da'
----------------------------------------



command> tr summary_by_year 2023


item #     amount     category   date       description
------------------------------------------------------------
2          100        mood       3/27/2023            'da'
3          10000      tuition    1/1/2023             "brandeis tuition"
----------------------------------------



command> tr summary_by_month 1  


item #     amount     category   date       description
------------------------------------------------------------
2          100        food       1/11/2022            "Some food"
1          100        food       1/1/2022             "Some food"
3          10000      tuition    1/1/2023             "brandeis tuition"
----------------------------------------



command> tr summary_by_category food


item #     amount     category   date       description
------------------------------------------------------------
2          100        food       1/11/2022            "Some food"
1          100        food       1/1/2022             "Some food"
----------------------------------------



command> tr show


item #     amount     category   date       description
------------------------------------------------------------
2          100        mood       3/27/2023            'da'
2          100        food       1/11/2022            "Some food"
1          100        food       1/1/2022             "Some food"
3          10000      tuition    1/1/2023             "brandeis tuition"
----------------------------------------



command> quit
PS F:\Qiongyue\study\Brandeis University\Spring 2023\CS 103A\cosi103a-team24-pa03> 
