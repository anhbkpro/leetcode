import pandas as pd


# My solution
def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    company_orders = pd.merge(orders, company, on='com_id')
    red_orders = company_orders[company_orders['name'] == 'RED']
    sales = pd.merge(sales_person, red_orders, on='sales_id', how='left')
    sales['com_id'] = sales['com_id'].fillna(0).astype(int)
    sales = sales[sales['com_id'] == 0]
    return pd.DataFrame({'name': sales['name_x']})


# LC solution
def sales_person_lc(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(orders, company, on='com_id')

    red_orders = df[df['name'] == 'RED']

    invalid_ids = red_orders.sales_id.unique()

    valid_sales_person = sales_person[~sales_person['sales_id'].isin(invalid_ids)]

    return valid_sales_person[['name']]