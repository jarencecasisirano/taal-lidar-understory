
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

# Load merged metrics + NDVI data
df = pd.read_csv("data/all_metrics_with_ndvi_100m.csv")

# Compute Pearson correlation
corr = df["NDVI_mean"].corr(df["voxel_occupancy_ratio"])
print(f"Pearson correlation: {corr:.3f}")

# Ensure output folder exists
output_dir = Path("data/plots")
output_dir.mkdir(parents=True, exist_ok=True)

# Plot
plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=df,
    x="voxel_occupancy_ratio",
    y="NDVI_mean",
    edgecolor="black",
    alpha=0.7
)
plt.title(f"NDVI vs. Voxel Cover Ratio (r = {corr:.3f})")
plt.xlabel("Voxel Occupancy Ratio (0.5–3.5 m)")
plt.ylabel("Mean NDVI")
plt.grid(True)
plt.tight_layout()

# Save plot
plot_path = output_dir / "ndvi_vs_voxel_cover.png"
plt.savefig(plot_path, dpi=300)
print(f"✅ Plot saved to {plot_path}")

# Show plot
plt.show()
