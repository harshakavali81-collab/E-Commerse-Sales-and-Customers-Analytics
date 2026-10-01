import pandas as pd
def test_totals():
    d = pd.read_csv("data/order_details.csv")
    assert len(d) == 31581
