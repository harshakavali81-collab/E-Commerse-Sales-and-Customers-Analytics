import pandas as pd
def load_clean():
    o = pd.read_csv("data/orders.csv")
    d = pd.read_csv("data/order_details.csv")
    return d.merge(o, on="order_id")
