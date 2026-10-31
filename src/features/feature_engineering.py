
import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/processed/purchase_orders_clean.csv")

# Convert date columns
df["OrderDate"] = pd.to_datetime(df["OrderDate"], errors="coerce")
df["ExpectedDeliveryDate"] = pd.to_datetime(
    df["ExpectedDeliveryDate"], errors="coerce"
)

# Extract date features
df["order_year"] = df["OrderDate"].dt.year
df["order_month"] = df["OrderDate"].dt.month
df["order_quarter"] = df["OrderDate"].dt.quarter
df["order_day_of_week"] = df["OrderDate"].dt.dayofweek

# Monday-Friday = 0, Saturday-Sunday = 1
df["is_weekend"] = (
    df["order_day_of_week"] >= 5
).astype("int")

# Create cost categories using dataset quantiles
df["cost_category"] = pd.qcut(
    df["TotalCost"],
    q=3,
    labels=["Low", "Medium", "High"],
    duplicates="drop"
)

# Display engineered features
features = [
    "PO_ID",
    "SupplierID",
    "TotalCost",
    "order_year",
    "order_month",
    "order_quarter",
    "order_day_of_week",
    "is_weekend",
    "planned_delivery_days",
    "cost_category"
]

print("\n========== ENGINEERED FEATURES ==========\n")
print(df[features].head(10).to_string(index=False))

print("\n========== FEATURE INFORMATION ==========\n")
print(df[features].info())

# Save engineered dataset
df.to_csv(
    "data/processed/purchase_orders_features.csv",
    index=False
)

print("\nFeature engineering completed successfully!")
