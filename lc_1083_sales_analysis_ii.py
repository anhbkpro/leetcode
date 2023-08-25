import pandas as pd


def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    m = sales.merge(product, on=['product_id'], how='inner')
    iphone_buyers = m[m['product_name'] == 'iPhone']['buyer_id'].drop_duplicates()
    s8_buyers = m[m['product_name'] == 'S8']['buyer_id'].drop_duplicates()
    s8_only_buyers = s8_buyers[~s8_buyers.isin(iphone_buyers)]

    return pd.DataFrame({'buyer_id': s8_only_buyers})
