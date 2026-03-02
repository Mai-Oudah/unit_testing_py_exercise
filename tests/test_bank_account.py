import pytest
from bank_account.bank_account import BankAccount


@pytest.fixture
def start_account():
    return BankAccount(100)
@pytest.fixture
def test_account():
    return BankAccount(200)

def test_deposit(start_account):
    start_account.deposit(50)
    assert start_account.balance == 150

def test_deposit_negative(start_account):
    with pytest.raises(ValueError, match="Deposit amount must be positive"):
        start_account.deposit(-50)
    
def test_withdraw(start_account):
    start_account.withdraw(21)
    assert start_account.balance==79

def test_withdraw_negative(start_account):
    with pytest.raises(ValueError, match="Withdraw amount must be positive"):
        start_account.withdraw(0)

def test_withdraw_insufficient(start_account):
    with pytest.raises(ValueError, match="Insufficient funds"):
        start_account.withdraw(143)

def test_transfer_to(start_account,test_account):
    start_account.transfer_to(test_account,32)
    assert start_account.balance == 68
    assert test_account.balance == 232
    
def test_transfer_to_not_bank_account(start_account,test_account):
    with pytest.raises(ValueError, match="Target must be a BankAccount"):
        start_account.transfer_to('platypus',32)

