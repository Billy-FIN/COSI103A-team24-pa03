# cosi103a-team24-pa03
This is a git repository which contains the code of programming assignment 03 (pa03) for cosi103a in Brandeis University.

## Collaborators:
 - Steve Wang ([Yell0wF1sh/github.com](https://github.com/Yell0wF1sh))
 - Qiuyang Wang https://github.com/Billy-FIN
 - Shentong Rao https://github.com/Shentongr


## Running Pylint
-------------------------------------------------------------------
PS C:\Users\steve\Documents\GitHub\cosi103a-team24-pa03\pa03> pylint tracker.py
************* Module tracker
tracker.py:76:0: R0912: Too many branches (18/12) (too-many-branches)

------------------------------------------------------------------
Your code has been rated at 9.85/10 (previous run: 9.85/10, +0.00)

PS C:\Users\steve\Documents\GitHub\cosi103a-team24-pa03\pa03> pylint transaction.py
************* Module transaction
transaction.py:16:0: W0611: Unused import os (unused-import)

------------------------------------------------------------------
Your code has been rated at 9.70/10 (previous run: 9.70/10, +0.00)

-------------------------------------------------------------------

## Running tracker.py

PS C:\Users\steve\Documents\GitHub\cosi103a-team24-pa03> & C:/Users/steve/AppData/Local/Microsoft/WindowsApps/python3.9.exe c:/Users/steve/Documents/GitHub/cosi103a-team24-pa03/pa03/tracker.py
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


item #          amount          category        date            description
--------------------------------------------------------------------------------
1               100             food            3/25/2023       "some food"
2               200             food            3/26/2023       "some more food"
3               50              misc            3/24/2023       "some misc"
4               500             food            3/28/2023       "a lot of food"
5               1000            school          1/1/2023        "paid tuition"
6               20000           car             8/26/2022       "bought a car"
----------------------------------------



command> tr delete 6
----------------------------------------



command> tr show


item #          amount          category        date            description
--------------------------------------------------------------------------------
1               100             food            3/25/2023       "some food"
2               200             food            3/26/2023       "some more food"
3               50              misc            3/24/2023       "some misc"
4               500             food            3/28/2023       "a lot of food"
5               1000            school          1/1/2023        "paid tuition"
----------------------------------------



command> tr add 7 20000 car 09/26/2022 "bought a car"
----------------------------------------



command> tr show


item #          amount          category        date            description
--------------------------------------------------------------------------------
1               100             food            3/25/2023       "some food"
2               200             food            3/26/2023       "some more food"
3               50              misc            3/24/2023       "some misc"
4               500             food            3/28/2023       "a lot of food"
5               1000            school          1/1/2023        "paid tuition"
7               20000           car             9/26/2022       "bought a car"
----------------------------------------



command> tr summary_by_date


item #          amount          category        date            description
--------------------------------------------------------------------------------
7               20000           car             9/26/2022       "bought a car"
5               1000            school          1/1/2023        "paid tuition"
3               50              misc            3/24/2023       "some misc"
1               100             food            3/25/2023       "some food"
2               200             food            3/26/2023       "some more food"
4               500             food            3/28/2023       "a lot of food"
----------------------------------------
