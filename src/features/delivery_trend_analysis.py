
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned purchase orders
df = pd.read_csv("data/processed/purchase_orders_clean.csv")

# Convert date column
df["OrderDate"] = pd.to_datetime(df["OrderDate"], errors="coerce")

# Remove rows without order dates
df = df.dropna(subset=["OrderDate", "Status"])

# Extract month from order date
df["order_month"] = df["OrderDate"].dt.to_period("M").astype(str)

# 1. Monthly order volume
monthly_orders = (
    df.groupby("order_month")
    .size()
    .reset_index(name="total_orders")
)

print("\n========== MONTHLY ORDER VOLUME ==========\n")
print(monthly_orders.to_string(index=False))

# 2. Monthly status distribution
monthly_status = pd.crosstab(
    df["order_month"],
    df["Status"]
)

print("\n========== MONTHLY STATUS DISTRIBUTION ==========\n")
print(monthly_status.to_string())

# 3. Monthly cancellation rate
monthly_cancellations = (
    df.assign(is_cancelled=(df["Status"] == "Cancelled").astype(int))
    .groupby("order_month")
    .agg(
        total_orders=("PO_ID", "count"),
        cancelled_orders=("is_cancelled", "sum")
    )
    .reset_index()
)

monthly_cancellations["cancellation_rate"] = (
    monthly_cancellations["cancelled_orders"]
    / monthly_cancellations["total_orders"]
    * 100
)

print("\n========== MONTHLY CANCELLATION RATE ==========\n")
print(monthly_cancellations.round(2).to_string(index=False))

# Save analysis results
monthly_orders.to_csv(
    "data/processed/monthly_orders.csv", index=False
)

monthly_status.to_csv(
    "data/processed/monthly_status.csv"
)

monthly_cancellations.to_csv(
    "data/processed/monthly_cancellations.csv", index=False
)

# Chart 1: Monthly order volume
plt.figure(figsize=(12, 5))
plt.plot(
    monthly_orders["order_month"],
    monthly_orders["total_orders"],
    marker="o"
)
plt.title("Monthly Purchase Order Volume")
plt.xlabel("Month")
plt.ylabel("Number of Orders")
plt.xticks(rotation=60)
plt.grid(True)
plt.tight_layout()
plt.savefig("data/processed/monthly_order_trend.png")
plt.show()

# Chart 2: Monthly cancellation rate
plt.figure(figsize=(12, 5))
plt.plot(
    monthly_cancellations["order_month"],
    monthly_cancellations["cancellation_rate"],
    marker="o"
)
plt.title("Monthly Cancellation Rate")
plt.xlabel("Month")
plt.ylabel("Cancellation Rate (%)")
plt.xticks(rotation=60)
plt.grid(True)
plt.tight_layout()
plt.savefig("data/processed/monthly_cancellation_trend.png")
plt.show()

print("\nDelivery trend analysis completed successfully!")
