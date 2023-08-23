import pandas as pd


def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    df = sales.merge(product, on=['product_id'])
    grouped = df.groupby('product_id')['quantity'].sum().reset_index()
    return grouped.rename(columns={'quantity': 'total_quantity'})
