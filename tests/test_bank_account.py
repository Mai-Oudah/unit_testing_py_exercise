import pytest
from bank_account.bank_account import BankAccount


def test_negative_initial_account():
    with pytest.raises(ValueError):
        BankAccount(-100)


def test_deposit_valid():
    acc = BankAccount(100)
    acc.deposit(50)
    assert acc.balance == 150


def test_invalid_deposit():
    acc = BankAccount(100)
    with pytest.raises(ValueError):
        acc.deposit(-50)
    assert acc.balance == 100


def test_withdraw_valid():
    acc = BankAccount(100)
    acc.withdraw(50)
    assert acc.balance == 50


def test_withdraw_negative():
    acc = BankAccount(100)
    with pytest.raises(ValueError):
        acc.withdraw(-50)
    assert acc.balance == 100


def test_withdraw_insufficient():
    acc = BankAccount(100)
    with pytest.raises(ValueError):
        acc.withdraw(1000)
    assert acc.balance == 100


def test_transfer_to_valid():
    acc1 = BankAccount(100)
    acc2 = BankAccount(0)
    acc1.transfer_to(acc2, 50)
    assert acc1.balance == 50
    assert acc2.balance == 50


def test_transfer_to_invalid_account():
    acc1 = BankAccount(100)
    with pytest.raises(ValueError):
        acc1.transfer_to("acc2", 50)
