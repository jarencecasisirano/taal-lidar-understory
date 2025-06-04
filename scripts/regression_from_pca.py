
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("data/all_metrics_with_ndvi_100m.csv")

# Select LiDAR metrics
X = df[[
    "canopy_cover_ratio_dbh",
    "voxel_occupancy_ratio",
    "fractional_cover",
    "normalized_cover",
    "lad_0.5_3.5m"
]]
y = df["NDVI_mean"]

# Perform PCA
pca = PCA()
X_pca = pca.fit_transform(X)
# Get feature names and PCA components
feature_names = X.columns.tolist()
loadings = pd.DataFrame(
    pca.components_.T,
    columns=[f"PC{i+1}" for i in range(len(pca.components_))],
    index=feature_names
)

# Print PC1 loadings
print("✅ PCA Loadings for PC1:")
print(loadings["PC1"])

# Print explained variance
print("✅ PCA Component Variance Explained:")
for i, var in enumerate(pca.explained_variance_ratio_):
    print(f"  PC{i+1}: {var:.3f}")

# Use first 2 PCs for regression
X_pc = X_pca[:, :2]
model = LinearRegression()
model.fit(X_pc, y)
y_pred = model.predict(X_pc)

# Evaluate regression
r2 = r2_score(y, y_pred)
print(f"\n✅ NDVI Regression using PC1 & PC2")
print(f"R²: {r2:.3f}")

# Plot actual vs predicted NDVI
plt.figure(figsize=(7, 6))
sns.scatterplot(x=y, y=y_pred, edgecolor='black', alpha=0.7)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', label='1:1 line')
plt.xlabel("Actual NDVI")
plt.ylabel("Predicted NDVI from PC1 + PC2")
plt.title(f"NDVI Prediction using PCA Components (R² = {r2:.3f})")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save plot
plt.savefig("data/plots/ndvi_pca_prediction.png", dpi=300)
plt.show()
