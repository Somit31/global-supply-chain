
import pandas as pd

# Load the original dataset
df = pd.read_csv("data/raw/purchase_order.csv")

# Clean column names and text values
df.columns = df.columns.str.strip()

for col in ["PO_ID", "SupplierID", "Status"]:
    df[col] = df[col].astype("string").str.strip()

# Convert dates and cost to proper data types
for col in ["OrderDate", "ExpectedDeliveryDate"]:
    df[col] = pd.to_datetime(df[col], errors="coerce")

df["TotalCost"] = pd.to_numeric(df["TotalCost"], errors="coerce")

# Recalculate planned delivery duration
df["planned_delivery_days"] = (
    df["ExpectedDeliveryDate"] - df["OrderDate"]
).dt.days

print("Original dataset shape:", df.shape)

# Remove rows missing essential information
df = df.dropna(
    subset=["PO_ID", "SupplierID", "OrderDate", "ExpectedDeliveryDate", "Status", "TotalCost"]
)

# Remove duplicate purchase order IDs
df = df.drop_duplicates(subset=["PO_ID"], keep="first")

# Keep valid delivery durations
df = df[df["planned_delivery_days"].between(1, 365)]

print("\nCleaned dataset shape:", df.shape)
print("\nRemaining missing values:")
print(df.isna().sum())

print("\nStatus distribution:")
print(df["Status"].value_counts())

print("\nSupplier summary:")
print(
    df.groupby("SupplierID")
    .agg(
        total_orders=("PO_ID", "count"),
        average_cost=("TotalCost", "mean"),
        average_planned_days=("planned_delivery_days", "mean"),
    )
    .round(2)
)

# Save cleaned data separately; preserve the original
df.to_csv("data/processed/purchase_orders_clean.csv", index=False)

print("\nCleaned dataset saved to data/processed/purchase_orders_clean.csv")
