
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load engineered dataset
df = pd.read_csv("data/processed/purchase_orders_features.csv")

# Select numerical features
numerical_df = df[
    [
        "TotalCost",
        "planned_delivery_days",
        "order_year",
        "order_month",
        "order_quarter",
        "order_day_of_week",
        "is_weekend",
    ]
]

# Calculate correlation matrix
correlation_matrix = numerical_df.corr()

print("\n========== CORRELATION MATRIX ==========\n")
print(correlation_matrix.round(2))

# Visualize correlation
plt.figure(figsize=(10, 7))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5
)

plt.title("Purchase Order Feature Correlation")
plt.tight_layout()

plt.savefig("data/processed/correlation_matrix.png")
plt.show()

print("\nCorrelation analysis completed!")
