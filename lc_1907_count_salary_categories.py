import pandas as pd


def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low = len(accounts[accounts['income'] < 20000])
    high = len(accounts[accounts['income'] > 50000])
    average = len(accounts) - low - high
    return pd.DataFrame(
        {'category': ['Low Salary', 'Average Salary', 'High Salary'], 'accounts_count': [low, average, high]}
    )


# LC solution
def count_salary_categories_lc(accounts: pd.DataFrame) -> pd.DataFrame:
    low_count = (accounts['income'] < 20000).sum()
    average_count = ((accounts['income'] >= 20000) & (accounts['income'] <= 50000)).sum()
    high_count = (accounts['income'] > 50000).sum()

    ans = pd.DataFrame({
        'category': ['Low Salary', 'Average Salary', 'High Salary'],
        'accounts_count': [low_count, average_count, high_count]
    })

    return ans
