import pandas as pd
from pathlib import Path

# Define paths to all metric files
data_dir = Path("data")

voxel = pd.read_csv(data_dir / "voxel_cover_metrics_100m.csv")
frac = pd.read_csv(data_dir / "fractional_cover_metrics_100m.csv")
norm = pd.read_csv(data_dir / "normalized_cover_metrics_100m.csv")
lad = pd.read_csv(data_dir / "lad_metrics_100m.csv")
canopy = pd.read_csv(data_dir / "canopy_cover_metrics_dbh_100m.csv")

# Merge all dataframes on 'tile'
merged = voxel.merge(frac, on="tile")
merged = merged.merge(norm, on="tile")
merged = merged.merge(lad, on="tile")
merged = merged.merge(canopy, on="tile")

# Save to a new CSV
output_path = data_dir / "all_metrics_100m.csv"
merged.to_csv(output_path, index=False)

print(f"✅ Merged all metrics to {output_path}")
