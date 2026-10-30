
import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/processed/purchase_orders_clean.csv")

# Analyze supplier performance
supplier_analysis = (
    df.groupby("SupplierID")
    .agg(
        total_orders=("PO_ID", "count"),
        average_order_cost=("TotalCost", "mean"),
        total_order_value=("TotalCost", "sum"),
        average_planned_days=("planned_delivery_days", "mean"),
        cancelled_orders=("Status", lambda x: (x == "Cancelled").sum()),
        delivered_orders=("Status", lambda x: (x == "Delivered").sum()),
    )
    .reset_index()
)

# Calculate cancellation percentage
supplier_analysis["cancellation_rate"] = (
    supplier_analysis["cancelled_orders"]
    / supplier_analysis["total_orders"]
    * 100
)

# Calculate delivery completion percentage
supplier_analysis["delivery_rate"] = (
    supplier_analysis["delivered_orders"]
    / supplier_analysis["total_orders"]
    * 100
)

supplier_analysis = supplier_analysis.round(2)

print("\n========== SUPPLIER PERFORMANCE ==========\n")
print(supplier_analysis.to_string(index=False))

# Save results
supplier_analysis.to_csv(
    "data/processed/supplier_analysis.csv",
    index=False
)

print("\nSupplier analysis saved successfully!")
