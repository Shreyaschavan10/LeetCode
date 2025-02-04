import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    n_customers = customers[~customers['id'].isin(orders['customerId'])]
    df= n_customers[['name']].rename(columns={'name': 'customers'})
    return df
