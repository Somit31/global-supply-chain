
import numpy as np
from sklearn.linear_model import LinearRegression

# 1. Historical delivery data
X = np.array([
    [100],
    [200],
    [300],
    [400],
    [500]
])

y = np.array([3.2, 4.8, 7.1, 8.2, 10.3])

# 2. Create the model
model = LinearRegression()

# 3. Train the model
model.fit(X, y)

# 4. Predict delivery time for a new shipment
new_distance = np.array([[250]])
prediction = model.predict(new_distance)

# 5. Display results
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)
print("Predicted delivery time:", prediction[0], "hours")