import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Create synthetic dataset
np.random.seed(42)
n_samples = 100

square_feet = np.random.randint(800, 4000, n_samples)
bedrooms = np.random.randint(1, 6, n_samples)
bathrooms = np.random.randint(1, 4, n_samples)

# Assume a simple formula for price with some noise
price = (square_feet * 200) + (bedrooms * 10000) + (bathrooms * 15000) + np.random.randint(-20000, 20000, n_samples)

# Build DataFrame
df = pd.DataFrame({
    'square_feet': square_feet,
    'bedrooms': bedrooms,
    'bathrooms': bathrooms,
    'price': price
})

# Features & Target
X = df[['square_feet', 'bedrooms', 'bathrooms']]
y = df['price']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))

# Coefficients
print("\nModel Coefficients:")
print(f"Square Footage: {model.coef_[0]:.2f}")
print(f"Bedrooms: {model.coef_[1]:.2f}")
print(f"Bathrooms: {model.coef_[2]:.2f}")
print(f"Intercept: {model.intercept_:.2f}")

# Example prediction
new_house = [[2500, 3, 2]]
predicted_price = model.predict(new_house)
print("\nPredicted price for new house:", int(predicted_price[0]))


plt.scatter(y_test, y_pred, alpha=0.7, color='blue')
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted House Prices")
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')
plt.show()
