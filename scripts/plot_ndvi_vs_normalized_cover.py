
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

# Load dataset
df = pd.read_csv("data/all_metrics_with_ndvi_100m.csv")

# Calculate Pearson correlation
corr = df["NDVI_mean"].corr(df["normalized_cover"])
print(f"Pearson correlation: {corr:.3f}")

# Ensure output directory exists
output_dir = Path("data/plots")
output_dir.mkdir(parents=True, exist_ok=True)

# Create scatterplot
plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=df,
    x="normalized_cover",
    y="NDVI_mean",
    edgecolor="black",
    alpha=0.7
)
plt.title(f"NDVI vs. Normalized Cover (r = {corr:.3f})")
plt.xlabel("Normalized Cover (Understory / First Returns)")
plt.ylabel("Mean NDVI")
plt.grid(True)
plt.tight_layout()

# Save plot
plot_path = output_dir / "ndvi_vs_normalized_cover.png"
plt.savefig(plot_path, dpi=300)
print(f"✅ Plot saved to {plot_path}")

# Show plot
plt.show()
