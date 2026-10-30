
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/supplier_analysis.csv")

# Chart 1: Total orders by supplier
plt.figure(figsize=(8, 5))
plt.bar(df["SupplierID"], df["total_orders"])
plt.title("Total Orders by Supplier")
plt.xlabel("Supplier")
plt.ylabel("Number of Orders")
plt.tight_layout()
plt.savefig("data/processed/total_orders.png")
plt.show()

# Chart 2: Cancellation rate
plt.figure(figsize=(8, 5))
plt.bar(df["SupplierID"], df["cancellation_rate"])
plt.title("Supplier Cancellation Rate")
plt.xlabel("Supplier")
plt.ylabel("Cancellation Rate (%)")
plt.tight_layout()
plt.savefig("data/processed/cancellation_rate.png")
plt.show()

# Chart 3: Average order cost
plt.figure(figsize=(8, 5))
plt.bar(df["SupplierID"], df["average_order_cost"])
plt.title("Average Order Cost by Supplier")
plt.xlabel("Supplier")
plt.ylabel("Average Cost")
plt.tight_layout()
plt.savefig("data/processed/average_order_cost.png")
plt.show()

print("All visualizations generated successfully!")
