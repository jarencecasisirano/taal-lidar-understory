
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/all_metrics_with_ndvi_100m.csv")

# Define predictors and target
X = df[[
    "canopy_cover_ratio_dbh",
    "voxel_occupancy_ratio",
    "fractional_cover",
    "normalized_cover",
    "lad_0.5_3.5m"
]]
y = df["NDVI_mean"]

# Fit linear regression
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

# Evaluate model
r2 = r2_score(y, y_pred)
mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)

print("✅ Linear Regression Results")
print(f"R²: {r2:.3f}")
print(f"RMSE: {rmse:.4f}")
print("Coefficients:")
for name, coef in zip(X.columns, model.coef_):
    print(f"  {name}: {coef:.4f}")

# Plot predicted vs. actual NDVI
plt.figure(figsize=(7, 6))
sns.scatterplot(x=y, y=y_pred, edgecolor='black', alpha=0.7)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', label='1:1 line')
plt.xlabel("Actual NDVI")
plt.ylabel("Predicted NDVI")
plt.title(f"NDVI Prediction from LiDAR Metrics (R² = {r2:.3f})")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save plot
plt.savefig("data/plots/ndvi_prediction_lidar.png", dpi=300)
plt.show()
