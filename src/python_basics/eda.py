import pandas as pd

df = pd.read_csv("data/raw/shipment.csv")

print("=== DATASET ===")
print(df)

print("\n=== BASIC INFORMATION ===")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nColumns:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\n=== DISTANCE ===")
print("Mean:", df["distance_km"].mean())
print("Median:", df["distance_km"].median())
print("Standard deviation:", df["distance_km"].std())
print("Minimum:", df["distance_km"].min())
print("Maximum:", df["distance_km"].max())

print("\n=== WEIGHT ===")
print("Mean:", df["weight_kg"].mean())
print("Median:", df["weight_kg"].median())
print("Standard deviation:", df["weight_kg"].std())
print("Minimum:", df["weight_kg"].min())
print("Maximum:", df["weight_kg"].max())

print("\n=== DELAYS ===")
print("Delayed shipments:", df["delayed"].sum())
print("Delay rate:", df["delayed"].mean() * 100, "%")

correlation = df["distance_km"].corr(df["delayed"])

print("Distance-delay correlation:", correlation)