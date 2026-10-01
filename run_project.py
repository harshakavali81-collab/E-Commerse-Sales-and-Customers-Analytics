import os
import time
import pandas as pd
from datetime import datetime

def print_header(title):
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70)

print_header("E-COMMERCE ENTERPRISE ANALYTICS: AUTOMATED PIPELINE EXECUTION")

# Step 1: Ingestion & Validation
print("\n[Step 1/4] Ingesting Star Schema Fact & Dimension Tables...")
time.sleep(0.5)
orders = pd.read_csv("data/orders.csv")
details = pd.read_csv("data/order_details.csv")
products = pd.read_csv("data/products.csv")
customers = pd.read_csv("data/customers.csv")

print(f"  -> Customers Table   : {len(customers):,} unique records loaded.")
print(f"  -> Products Table    : {len(products):,} active catalog items loaded.")
print(f"  -> Orders Table      : {len(orders):,} transaction headers loaded.")
print(f"  -> Order Details     : {len(details):,} line items loaded.")

# Step 2: Merge & Financial Reconciliation
print("\n[Step 2/4] Joining Relational Dimensions & Calculating Financial KPIs...")
time.sleep(0.5)
df = details.merge(orders, on="order_id").merge(products, on="product_id").merge(customers, on="customer_id")
completed = df[df["order_status"] == "Completed"].copy()

net_revenue = completed["revenue"].sum()
gross_profit = completed["profit"].sum()
gross_margin = (gross_profit / net_revenue) * 100
order_count = completed["order_id"].nunique()
customer_count = completed["customer_id"].nunique()
aov = net_revenue / order_count

print_header("RECONCILED FINANCIAL EXECUTIVE DASHBOARD")
print(f"  • Total Net Revenue     : INR {net_revenue:,.2f}")
print(f"  • Total Gross Profit    : INR {gross_profit:,.2f}")
print(f"  • Gross Profit Margin   : {gross_margin:.2f}%")
print(f"  • Completed Order Count : {order_count:,} orders")
print(f"  • Active Customer Base  : {customer_count:,} customers")
print(f"  • Average Order Value   : INR {aov:,.2f}")

# Step 3: Run Customer RFM Behavioral Segmentation
print("\n[Step 3/4] Generating Customer Recency-Frequency-Monetary (RFM) Model...")
time.sleep(0.5)
completed["order_date"] = pd.to_datetime(completed["order_date"])
ref_date = completed["order_date"].max() + pd.Timedelta(days=1)

rfm = completed.groupby("customer_id").agg({
    "order_date": lambda x: (ref_date - x.max()).days,
    "order_id": "nunique",
    "revenue": "sum"
}).reset_index()

rfm.columns = ["customer_id", "recency", "frequency", "monetary"]
rfm["r_score"] = pd.qcut(rfm["recency"], 5, labels=[5, 4, 3, 2, 1]).astype(int)
rfm["f_score"] = pd.qcut(rfm["frequency"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5]).astype(int)
rfm["m_score"] = pd.qcut(rfm["monetary"], 5, labels=[1, 2, 3, 4, 5]).astype(int)

def segment_customer(r):
    if r["r_score"] >= 4 and r["f_score"] >= 4 and r["m_score"] >= 4:
        return "Champions"
    elif r["f_score"] >= 3 and r["m_score"] >= 3:
        return "Loyal Customers"
    elif r["r_score"] <= 2 and r["f_score"] >= 3:
        return "At Risk"
    else:
        return "Standard / Hibernating"

rfm["segment"] = rfm.apply(segment_customer, axis=1)
rfm.to_csv("outputs/rfm_customer_segments.csv", index=False)

print("  -> RFM Segmentation Breakdown:")
for segment, count in rfm["segment"].value_counts().items():
    pct = (count / len(rfm)) * 100
    print(f"     - {segment:<24} : {count:5,} customers ({pct:.1f}%)")

# Step 4: Verification Checks
print("\n[Step 4/4] Verifying System Assertions...")
assert round(net_revenue, 2) == 211448183.45, "Revenue mismatch!"
assert round(gross_profit, 2) == 63272309.05, "Profit mismatch!"
assert order_count == 31581, "Order count mismatch!"
assert customer_count == 5376, "Customer count mismatch!"

print_header("ALL 4 INTEGRATION CHECKS PASSED: SYSTEM FULLY OPERATIONAL")
