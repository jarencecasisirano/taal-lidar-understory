
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

# Load dataset
df = pd.read_csv("data/all_metrics_with_ndvi_100m.csv")

# Calculate Pearson correlation
corr = df["NDVI_mean"].corr(df["fractional_cover"])
print(f"Pearson correlation: {corr:.3f}")

# Ensure output folder exists
output_dir = Path("data/plots")
output_dir.mkdir(parents=True, exist_ok=True)

# Plot
plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=df,
    x="fractional_cover",
    y="NDVI_mean",
    edgecolor="black",
    alpha=0.7
)
plt.title(f"NDVI vs. Fractional Cover (r = {corr:.3f})")
plt.xlabel("Fractional Cover (0.5–3.5 m)")
plt.ylabel("Mean NDVI")
plt.grid(True)
plt.tight_layout()

# Save figure
plot_path = output_dir / "ndvi_vs_fractional_cover.png"
plt.savefig(plot_path, dpi=300)
print(f"✅ Plot saved to {plot_path}")

# Show plot
plt.show()
