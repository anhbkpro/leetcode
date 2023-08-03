import pandas as pd


# Approach 1: Filtering Data with Exclusion Criteria
def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Select the rows which `id` is not present in orders['customerId'].
    df = customers[~customers['id'].isin(orders['customerId'])]

    # Build a dataframe that only contains the column `name`
    # and rename the column `name` as `Customers`.
    df = df[['name']].rename(columns={'name': 'Customers'})
    return df


# Approach 2: Left Join on customers
def customers_who_never_order(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = customers.merge(orders, left_on='id', right_on='customerId', how='left')
    df = df[df['customerId'].isna()]
    df = df[['name']].rename(columns={'name': 'Customers'})
    return df
