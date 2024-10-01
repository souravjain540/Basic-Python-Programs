import numpy as np
import matplotlib.pyplot as plt

# Sample Data (Height vs. Weight, for example)
# X represents height in cm, Y represents weight in kg
X = np.array([150, 160, 170, 180, 190])
Y = np.array([50, 60, 65, 70, 80])
n = len(X)

# Mean of X and Y
mean_x = np.mean(X)
mean_y = np.mean(Y)

# Calculating the coefficients for Linear Regression
numerator = np.sum((X - mean_x) * (Y - mean_y))  # Σ((Xi - X̄) * (Yi - Ȳ))
denominator = np.sum((X - mean_x) ** 2)  # Σ((Xi - X̄)^2)

# Slope (m) and Intercept (b) for y = mx + b
m = numerator / denominator  # Slope
b = mean_y - (m * mean_x)    # Intercept

print(f"Slope (m): {m}")
print(f"Intercept (b): {b}")

# Prediction using the regression model
def predict(x):
    return m * x + b

# Predicted values for X
Y_pred = predict(X)

# Plotting the results
plt.scatter(X, Y, color="blue", label="Data Points")  # Plot original data points
plt.plot(X, Y_pred, color="red", label="Regression Line")  # Plot regression line

plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.title("Linear Regression Example")
plt.legend()

# Save the plot as an image file
plt.savefig("linear_regression_plot.png")
print("Plot saved as 'linear_regression_plot.png'")
