import pandas as pd

df = pd.read_csv("data/raw/dirty_shipments.csv")

print("Original data:")
print(df)

# 1. Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# 2. Remove duplicate rows
df = df.drop_duplicates()

# 3. Remove invalid negative weights
df = df[df["weight_kg"] >= 0]

# 4. Fill missing weight with median
df["weight_kg"] = df["weight_kg"].fillna(
    df["weight_kg"].median()
)

# 5. Fill missing distance with median
df["distance_km"] = df["distance_km"].fillna(
    df["distance_km"].median()
)

# 6. Standardize origin names
df["origin"] = df["origin"].str.strip().str.title()

print("\nCleaned data:")
print(df)

df["distance_km"].quantile(0.25)