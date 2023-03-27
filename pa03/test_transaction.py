import pytest
from transaction import Transaction
"""
this is test for transaction.py, goal is to test do the function in transaction.py run well
@Author Shentong Rao
"""

"""
this is creating a new transaction
@Author Shentonf Rao
"""
@pytest.fixture
def transaction():
    # Create an instance of the Transaction class to be used in tests
    return Transaction()

"""
this is test for add method and show method
@Author Shentong Rao
"""

def test_add_and_show(transaction):
    # creating a transaction to be added to the database
    new_transaction = {'itemID': '1',
                       'amount': 50,
                       'category': 'groceries',
                       'date': '03/27/2023',
                       'description': 'Bought groceries'}
    
    # Call the add method to add the transaction
    transaction.add(new_transaction)
    
    # Assert that the transaction was actually added by calling the show method and make sure the show method is running correctly
    assert transaction.show() == [{'itemID': '1',
                                   'amount': 50,
                                   'category': 'groceries',
                                   'day': 27,
                                   'month': 3,
                                   'year': 2023,
                                   'description': 'Bought groceries'}]

"""
this is test summary by date method
@Author Shentong Rao
"""

def test_sum_by_date(transaction):
    # Test summing transactions by date
    assert transaction.sum_by_date() == [{'itemID': '1', 
                                           'amount': 50, 
                                           'category': 'groceries', 
                                           'day': 27, 
                                           'month': 3, 
                                           'year': 2023, 
                                           'description': 'Bought groceries'}]


"""
this is test summary by month method
@Author Shentong Rao
"""

def test_sum_by_month(transaction):
    # Test summing transactions by month 
    assert transaction.sum_by_month(3) == [{'itemID': '1', 
                                            'amount': 50,
                                            'category': 'groceries', 
                                            'day': 27, 'month': 3, 
                                            'year': 2023, 
                                            'description': 'Bought groceries'}]


"""
this is test summary by year method
@Author Shentong Rao
"""

def test_sum_by_year(transaction):
    # Test summing transactions by year
    assert transaction.sum_by_year(2023) == [{'itemID': '1', 
                                              'amount': 50, 
                                              'category': 'groceries', 
                                              'day': 27, 'month': 3, 
                                              'year': 2023, 
                                              'description': 'Bought groceries'}]


"""
this is test summary by category method
@Author Shentong Rao
"""

def test_sum_by_cate(transaction):
    # Test summing transactions by category
    assert transaction.sum_by_cate('groceries') == [{'itemID': '1', 
                                                     'amount': 50, 
                                                     'category': 'groceries', 
                                                     'day': 27, 'month': 3, 
                                                     'year': 2023, 
                                                     'description': 'Bought groceries'}]


"""
this is test delete method
@Author Shentong Rao
"""

def test_delete(transaction):
    # Test deleting a transaction
    transaction.delete('1')
    assert transaction.show() == []

