import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Load your combined dataset
df = pd.read_csv("data/all_metrics_with_ndvi_100m.csv")

# Select the five LiDAR-derived structural metrics
metrics = df[[
    "canopy_cover_ratio_dbh",
    "voxel_occupancy_ratio",
    "fractional_cover",
    "normalized_cover",
    "lad_0.5_3.5m"
]]

# Standardize the metrics
scaler = StandardScaler()
metrics_scaled = scaler.fit_transform(metrics)

# Apply PCA (keep first 2 components)
pca = PCA(n_components=2)
components = pca.fit_transform(metrics_scaled)

# Add PC1 and PC2 to the original dataframe
df["PC1"] = components[:, 0]
df["PC2"] = components[:, 1]

# (Optional) Save updated dataset
df.to_csv("data/all_metrics_with_ndvi_and_pca.csv", index=False)

# Preview result
print(df[["tile", "PC1", "PC2", "NDVI_mean"]].head())
