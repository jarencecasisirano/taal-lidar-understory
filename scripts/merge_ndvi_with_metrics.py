import pandas as pd
from pathlib import Path

# Load data
lidar_metrics = pd.read_csv("data/all_metrics_100m.csv")
ndvi_stats = pd.read_csv("data/ndvi_tile_stats_2017.csv")

# Preview column names in NDVI stats to check match
print("NDVI columns:", ndvi_stats.columns)

# If the tile name column differs, rename it for consistency
if "tile" not in ndvi_stats.columns:
    ndvi_stats.rename(columns={"your_tile_column_name_here": "tile"}, inplace=True)

# Merge by 'tile' column
merged = lidar_metrics.merge(ndvi_stats, on="tile", how="inner")

# Save result
output_path = Path("data/all_metrics_with_ndvi_100m.csv")
merged.to_csv(output_path, index=False)

print(f"✅ Merged metrics and NDVI stats saved to {output_path}")
