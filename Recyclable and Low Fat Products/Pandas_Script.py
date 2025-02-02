import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    low_fat_1=products['low_fats']=='Y'
    recyclable_1=products['recyclable']=='Y'

    find_products= products[low_fat_1 & recyclable_1][['product_id']]
    return find_products
