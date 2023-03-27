# cosi103a-team24-pa03
This is a git repository which contains the code of programming assignment 03 (pa03) for cosi103a in Brandeis University.

The program allows users to do different operations to a database which contains information of transactions. Users can add,
delete, show transactions selected by category, and so on.

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

![console log 1](/img/console1.JPG)
![console log 2](/img/console2.JPG)
![console log 3](/img/console3.JPG)

## this is running for pytest

pytest -v
====================================================================================== test session starts ======================================================================================
platform darwin -- Python 3.7.6, pytest-5.3.5, py-1.8.1, pluggy-0.13.1 -- /Users/raoshentong/opt/anaconda3/bin/python
cachedir: .pytest_cache
hypothesis profile 'default' -> database=DirectoryBasedExampleDatabase('/Users/raoshentong/Desktop/cosi103a-team24-pa03/.hypothesis/examples')
rootdir: /Users/raoshentong/Desktop/cosi103a-team24-pa03
plugins: hypothesis-5.5.4, arraydiff-0.3, remotedata-0.3.2, openfiles-0.4.0, doctestplus-0.5.0, anyio-3.6.2, astropy-header-0.1.2
collected 6 items                                                                                                                                                                               

pa03/test_transaction.py::test_add_and_show PASSED                                                                                                                                        [ 16%]
pa03/test_transaction.py::test_sum_by_date PASSED                                                                                                                                         [ 33%]
pa03/test_transaction.py::test_sum_by_month PASSED                                                                                                                                        [ 50%]
pa03/test_transaction.py::test_sum_by_year PASSED                                                                                                                                         [ 66%]
pa03/test_transaction.py::test_sum_by_cate PASSED                                                                                                                                         [ 83%]
pa03/test_transaction.py::test_delete PASSED                                                                                                                                              [100%]

======================================================================================= 6 passed in 0.09s =======================================================================================
