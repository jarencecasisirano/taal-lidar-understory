
import laspy
import numpy as np
import pandas as pd
from pathlib import Path

# Paths
input_dir = Path("data/normalized_las")
output_csv = Path("data/fractional_cover_metrics.csv")

# Height range for understory
min_height = 0.5
max_height = 3.5

results = []

for file in input_dir.glob("*.las"):
    print(f"Processing {file.name}...")
    las = laspy.read(file)
    z = las.z
    classifications = las.classification

    # Count ground points (class = 2)
    ground_mask = classifications == 2
    ground_count = np.count_nonzero(ground_mask)

    # Count vegetation points in understory height range (class ≠ 2)
    veg_mask = (z >= min_height) & (z <= max_height) & (classifications != 2)
    veg_count = np.count_nonzero(veg_mask)

    # Compute fractional cover
    denominator = veg_count + ground_count
    frac = veg_count / denominator if denominator > 0 else 0.0

    print(f"  Ground: {ground_count}, Vegetation: {veg_count}, FRAC = {frac:.4f}")

    results.append({
        "tile": file.name,
        "understory_veg_returns": veg_count,
        "ground_returns": ground_count,
        "fractional_cover": round(frac, 4)
    })

# Save to CSV
df = pd.DataFrame(results)
df.to_csv(output_csv, index=False)
print(f"✅ Fractional cover metrics saved to {output_csv}")
