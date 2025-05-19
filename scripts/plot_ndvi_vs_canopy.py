
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

# Load merged metrics + NDVI data
df = pd.read_csv("data/all_metrics_with_ndvi_100m.csv")

# Compute Pearson correlation
corr = df["NDVI_mean"].corr(df["canopy_cover_ratio_dbh"])
print(f"Pearson correlation: {corr:.3f}")

# Ensure output folder exists
output_dir = Path("data/plots")
output_dir.mkdir(parents=True, exist_ok=True)

# Plot
plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=df,
    x="canopy_cover_ratio_dbh",
    y="NDVI_mean",
    edgecolor="black",
    alpha=0.7
)
plt.title(f"NDVI vs. Canopy Cover Ratio (r = {corr:.3f})")
plt.xlabel("Canopy Cover Ratio (DBH-based)")
plt.ylabel("Mean NDVI")
plt.grid(True)
plt.tight_layout()

# Save plot
plot_path = output_dir / "ndvi_vs_canopy_cover.png"
plt.savefig(plot_path, dpi=300)
print(f"✅ Plot saved to {plot_path}")

# Also display the plot
plt.show()
