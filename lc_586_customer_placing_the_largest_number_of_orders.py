import pandas as pd


# My solution
def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    df = orders.groupby('customer_number')['order_number'].nunique().reset_index()
    df = df.sort_values(by=['order_number'])
    return df[['customer_number']].tail(1)
