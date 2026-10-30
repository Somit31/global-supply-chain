
import pandas as pd

file_path = "data/raw/purchase_order_dataset.csv"

df = pd.read_csv(file_path)

# Clean whitespace from column names and text values
df.columns = df.columns.str.strip()

for col in ["PO_ID", "SupplierID", "Status"]:
    df[col] = df[col].astype("string").str.strip()

# Parse dates
for col in ["OrderDate", "ExpectedDeliveryDate"]:
    df[col] = pd.to_datetime(df[col], errors="coerce")

# Calculate planned delivery duration
df["planned_delivery_days"] = (
    df["ExpectedDeliveryDate"] - df["OrderDate"]
).dt.days

print("Dataset shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nFirst 10 rows:")
print(df.head(10).to_string(index=False))

print("\nMissing values:")
print(df.isna().sum())

print("\nOrder status counts:")
print(df["Status"].value_counts(dropna=False))

print("\nPlanned delivery duration:")
print(df["planned_delivery_days"].describe())
