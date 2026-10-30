
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Historical shipment data

import numpy as np

# Generate 100 shipment distances
np.random.seed(42)
X = np.random.randint(50, 1000, size=(100, 1))

# Simulate delivery time with some random variation
y = 1 + 0.02 * X.ravel() + np.random.normal(0, 1, size=100)


# 1. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))

# 2. Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# 3. Predict on unseen test data
y_pred = model.predict(X_test)

# 4. Evaluate the model
print("Actual values:", y_test)
print("Predicted values:", y_pred)
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))
