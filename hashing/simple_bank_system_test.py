from .simple_bank_system import Bank

def test_withdraw_success():
    b = Bank([100, 200, 300])
    result = b.withdraw(2, 150)
    assert result is True
    assert b.balance == [100, 50, 300]

def test_withdraw_exact_balance():
    b = Bank([50])
    result = b.withdraw(1, 50)
    assert result is True
    assert b.balance == [0]

def test_withdraw_insufficient_funds():
    b = Bank([100])
    result = b.withdraw(1, 200)
    assert result is False
    assert b.balance == [100]

def test_withdraw_invalid_account():
    b = Bank([100, 200])
    result = b.withdraw(3, 50)
    assert result is False
    assert b.balance == [100, 200]
