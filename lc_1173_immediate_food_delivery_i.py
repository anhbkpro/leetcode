import pandas as pd


def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    immediate_orders = len(delivery[delivery['order_date'] == delivery['customer_pref_delivery_date']])
    total = len(delivery)
    return pd.DataFrame({'immediate_percentage': [round(immediate_orders / total * 100, 2)]})
