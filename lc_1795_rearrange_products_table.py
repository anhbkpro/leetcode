import pandas as pd


def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    # Filter rows that have a null value in the 'store1' column
    # and select columns 'product_id' and 'store1'.
    a = products.loc[products['store1'].notnull(), ['product_id', 'store1']]
    # We create a new column store to the DataFrame a and set all its values to the string "store1".
    a['store'] = 'store1'
    # We rename the column store1 to price.
    a.rename(columns={'store1': 'price'}, inplace=True)
    # Since the order of the columns may not be in the desired sequence, the last step is to rearrange the columns to
    # the desired order. Now the order of the store and price columns has been rearranged to match the expected output.
    a = a[['product_id', 'store', 'price']]

    b = products.loc[products['store2'].notnull(), ['product_id', 'store2']]
    b['store'] = 'store2'
    b.rename(columns={'store2': 'price'}, inplace=True)
    b = b[['product_id', 'store', 'price']]

    c = products.loc[products['store3'].notnull(), ['product_id', 'store3']]
    c['store'] = 'store3'
    c.rename(columns={'store3': 'price'}, inplace=True)
    c = c[['product_id', 'store', 'price']]

    answer = pd.concat([a, b, c])
    return answer
