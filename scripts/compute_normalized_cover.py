
import laspy
import numpy as np
import pandas as pd
from pathlib import Path

# Paths
input_dir = Path("data/normalized_las_100m")
output_csv = Path("data/normalized_cover_metrics_100m.csv")

# Understory height range
min_height = 0.5
max_height = 3.5

results = []

for file in input_dir.glob("*.las"):
    print(f"Processing {file.name}...")
    las = laspy.read(file)
    z = las.z
    classifications = las.classification
    return_nums = las.return_number

    # Total number of first returns
    total_first_returns = np.count_nonzero(return_nums == 1)

    # Understory vegetation returns (0.5–3.5m, class ≠ 2)
    norm_mask = (z >= min_height) & (z <= max_height) & (classifications != 2)
    understory_returns = np.count_nonzero(norm_mask)

    # Normalized Cover
    norm = understory_returns / total_first_returns if total_first_returns > 0 else 0.0

    print(f"  First returns: {total_first_returns}, Understory returns: {understory_returns}, NORM = {norm:.4f}")

    results.append({
        "tile": file.name,
        "understory_returns": understory_returns,
        "first_returns": total_first_returns,
        "normalized_cover": round(norm, 4)
    })

# Save to CSV
df = pd.DataFrame(results)
df.to_csv(output_csv, index=False)
print(f"✅ Normalized cover metrics saved to {output_csv}")
