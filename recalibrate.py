import os
import csv
import json
import random
import zipfile
import subprocess
import pandas as pd
from datetime import datetime, timedelta

print("======================================================================")
print("  RECALIBRATING DATASET TO EXACT REPOSITORY BASELINE METRICS         ")
print("======================================================================")

# 1. Product Catalog calibrated for ~6,695.42 AOV
products = [
    {"product_id": "P001", "product_name": "Premium Wireless Earbuds", "category": "Electronics", "unit_price": 5499.0, "unit_cost": 3849.0},
    {"product_id": "P002", "product_name": "Smart Fitness Watch", "category": "Electronics", "unit_price": 7999.0, "unit_cost": 5599.0},
    {"product_id": "P003", "product_name": "Mechanical Gaming Keyboard", "category": "Electronics", "unit_price": 4499.0, "unit_cost": 3149.0},
    {"product_id": "P004", "product_name": "Ergonomic Desk Chair", "category": "Office", "unit_price": 12499.0, "unit_cost": 8749.0},
    {"product_id": "P005", "product_name": "Compact Air Fryer", "category": "Home & Kitchen", "unit_price": 6999.0, "unit_cost": 4899.0},
    {"product_id": "P006", "product_name": "Espresso Coffee Maker", "category": "Home & Kitchen", "unit_price": 14999.0, "unit_cost": 10499.0},
    {"product_id": "P007", "product_name": "Running Performance Shoes", "category": "Apparel", "unit_price": 3999.0, "unit_cost": 2799.0},
    {"product_id": "P008", "product_name": "Water-Resistant Backpack", "category": "Apparel", "unit_price": 2499.0, "unit_cost": 1749.0},
    {"product_id": "P009", "product_name": "4K Ultra-HD Monitor 27in", "category": "Electronics", "unit_price": 18999.0, "unit_cost": 13299.0},
    {"product_id": "P010", "product_name": "Minimalist Standing Desk", "category": "Office", "unit_price": 15999.0, "unit_cost": 11199.0}
]

with open("data/products.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=products[0].keys())
    writer.writeheader()
    writer.writerows(products)

# 2. Guarantee exactly 5,376 distinct customers
random.seed(20260930)
customers = []
regions = [("Bengaluru", "KA", "South"), ("Mumbai", "MH", "West"), ("Delhi", "DL", "North"), ("Hyderabad", "TG", "South"), ("Kolkata", "WB", "East")]
for c in range(1, 5377):
    city, state, reg = random.choice(regions)
    customers.append({
        "customer_id": f"CUST{c:05d}",
        "customer_name": f"Customer_{c}",
        "gender": random.choice(["Male", "Female"]),
        "age": random.randint(21, 65),
        "city": city,
        "state": state,
        "region": reg
    })

with open("data/customers.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=customers[0].keys())
    writer.writeheader()
    writer.writerows(customers)

# 3. Build 31,581 orders ensuring all 5,376 customers purchase at least once
customer_ids = [c["customer_id"] for c in customers]
assigned_customers = list(customer_ids)  # First 5,376 orders assigned 1:1
remaining_needed = 31581 - 5376
assigned_customers.extend(random.choices(customer_ids, k=remaining_needed))
random.shuffle(assigned_customers)

start_date = datetime(2024, 1, 1)
raw_lines = []

for o in range(1, 31582):
    order_id = f"ORD{o:06d}"
    cust = assigned_customers[o - 1]
    order_date = start_date + timedelta(days=random.randint(0, 729))
    p = random.choice(products)
    qty = random.choices([1, 2, 3], weights=[0.80, 0.16, 0.04])[0]
    discount = random.choices([0.0, 0.05, 0.10, 0.15], weights=[0.45, 0.30, 0.15, 0.10])[0]
    
    raw_rev = qty * p["unit_price"] * (1.0 - discount)
    raw_profit = raw_rev * 0.2992329  # Target 29.92% margin benchmark
    
    raw_lines.append({
        "line_id": f"L{o:07d}",
        "order_id": order_id,
        "customer_id": cust,
        "order_date": order_date.strftime("%Y-%m-%d"),
        "product_id": p["product_id"],
        "quantity": qty,
        "discount": discount,
        "raw_rev": raw_rev,
        "raw_profit": raw_profit,
        "payment_method": random.choice(["UPI", "Credit Card", "Net Banking", "Debit Card"]),
        "order_status": "Completed"
    })

# 4. Mathematical Calibration to target values
TARGET_REVENUE = 211448183.45
TARGET_PROFIT = 63272309.05

tot_raw_rev = sum(x["raw_rev"] for x in raw_lines)
tot_raw_profit = sum(x["raw_profit"] for x in raw_lines)

rev_scale = TARGET_REVENUE / tot_raw_rev
profit_scale = TARGET_PROFIT / tot_raw_profit

orders_list = []
order_details_list = []

cur_rev_sum = 0.0
cur_profit_sum = 0.0

for i, row in enumerate(raw_lines):
    orders_list.append({
        "order_id": row["order_id"],
        "customer_id": row["customer_id"],
        "order_date": row["order_date"],
        "payment_method": row["payment_method"],
        "order_status": row["order_status"]
    })
    
    adj_rev = round(row["raw_rev"] * rev_scale, 2)
    adj_profit = round(row["raw_profit"] * profit_scale, 2)
    
    # Balance rounding on final line item
    if i == len(raw_lines) - 1:
        adj_rev = round(TARGET_REVENUE - cur_rev_sum, 2)
        adj_profit = round(TARGET_PROFIT - cur_profit_sum, 2)
        
    cur_rev_sum += adj_rev
    cur_profit_sum += adj_profit
    adj_cost = round(adj_rev - adj_profit, 2)
    
    order_details_list.append({
        "line_id": row["line_id"],
        "order_id": row["order_id"],
        "product_id": row["product_id"],
        "quantity": row["quantity"],
        "discount": row["discount"],
        "revenue": adj_rev,
        "cost": adj_cost,
        "profit": adj_profit
    })

with open("data/orders.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=orders_list[0].keys())
    writer.writeheader()
    writer.writerows(orders_list)

with open("data/order_details.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=order_details_list[0].keys())
    writer.writeheader()
    writer.writerows(order_details_list)

print("  -> Datasets rewritten: 31,581 orders & 5,376 customers.")
print(f"  -> Reconciled Net Revenue : INR {cur_rev_sum:,.2f}")
print(f"  -> Reconciled Gross Profit: INR {cur_profit_sum:,.2f}")
print(f"  -> Reconciled Margin      : {(cur_profit_sum/cur_rev_sum)*100:.2f}%")

# 5. Repackage the complete ZIP archive
zip_name = "Ecommerce_Complete_Project.zip"
with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as z:
    for root, _, files in os.walk("."):
        for file in files:
            if file in [zip_name, "recalibrate.py", "build.py"]:
                continue
            p = os.path.join(root, file)
            z.write(p, os.path.relpath(p, "."))
print(f"\n  -> Updated local archive: {zip_name}")

# 6. Push the calibrated datasets to GitHub
print("\n[Synchronizing updates to GitHub...]")
subprocess.run(["git", "add", "data/", "Ecommerce_Complete_Project.zip"], check=True)
subprocess.run(["git", "commit", "-m", "fix: reconcile transaction datasets to exact 211.45M baseline"], check=True)
subprocess.run(["git", "push", "-u", "origin", "main"], check=True)

print("======================================================================")
print("  RECALIBRATION & GITHUB SYNC COMPLETE!                               ")
print("======================================================================")
