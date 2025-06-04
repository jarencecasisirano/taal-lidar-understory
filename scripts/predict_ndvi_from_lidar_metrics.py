import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path

# Load dataset
df = pd.read_csv("data/all_metrics_with_ndvi_100m.csv")

# Select predictor variables (LiDAR metrics)
X = df[[
    "canopy_cover_ratio_dbh",
    "voxel_occupancy_ratio",
    "fractional_cover",
    "normalized_cover",
    "lad_0.5_3.5m"
]]

# Target variable
y = df["NDVI_mean"]

# Split dataset (70% train, 30% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Train linear regression model
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Evaluate performance
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

# Plot actual vs predicted NDVI
plt.figure(figsize=(8, 6))
sns.scatterplot(x=y_test, y=y_pred, edgecolor='black', alpha=0.7)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', label='1:1 line')
plt.xlabel("Actual NDVI")
plt.ylabel("Predicted NDVI (from LiDAR metrics)")
plt.title(f"NDVI Prediction from LiDAR Metrics (R² = {r2:.3f}, RMSE = {rmse:.4f})")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save plot
Path("data/plots").mkdir(parents=True, exist_ok=True)
plt.savefig("data/plots/ndvi_lidar_prediction_v2.png", dpi=300)
