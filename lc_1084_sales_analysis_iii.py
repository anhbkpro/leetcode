import pandas as pd


def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    m = sales.merge(product, on=['product_id'], how='inner')
    start_date = pd.Timestamp('2019-01-01')
    end_date = pd.Timestamp('2019-03-31')
    out_product_ids = m[(m['sale_date'] > end_date) | (m['sale_date'] < start_date)]['product_id'].drop_duplicates()
    return m[~m['product_id'].isin(out_product_ids)][['product_id', 'product_name']].drop_duplicates()
