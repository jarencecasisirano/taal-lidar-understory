
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

# Load data
df = pd.read_csv("data/all_metrics_with_ndvi_100m.csv")

# Calculate Pearson correlation
corr = df["NDVI_mean"].corr(df["lad_0.5_3.5m"])
print(f"Pearson correlation: {corr:.3f}")

# Prepare output folder
output_dir = Path("data/plots")
output_dir.mkdir(parents=True, exist_ok=True)

# Create scatterplot
plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=df,
    x="lad_0.5_3.5m",
    y="NDVI_mean",
    edgecolor="black",
    alpha=0.7
)
plt.title(f"NDVI vs. Leaf Area Density (r = {corr:.3f})")
plt.xlabel("Leaf Area Density (0.5–3.5 m)")
plt.ylabel("Mean NDVI")
plt.grid(True)
plt.tight_layout()

# Save plot
plot_path = output_dir / "ndvi_vs_lad.png"
plt.savefig(plot_path, dpi=300)
print(f"✅ Plot saved to {plot_path}")

# Show plot
plt.show()
