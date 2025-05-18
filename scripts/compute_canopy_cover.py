
import laspy
import numpy as np
import pandas as pd
from pathlib import Path

# Paths
input_dir = Path("data/normalized_las")
output_csv = Path("data/canopy_cover_metrics_dbh.csv")

# Canopy height threshold based on DBH standard
canopy_cutoff = 1.37

results = []

for file in input_dir.glob("*.las"):
    print(f"Processing {file.name}...")
    las = laspy.read(file)
    z = las.z
    return_nums = las.return_number

    # Filter for first returns only
    first_returns_mask = return_nums == 1
    total_first_returns = np.count_nonzero(first_returns_mask)

    # Among first returns, count those above the cutoff
    canopy_returns = np.count_nonzero((z > canopy_cutoff) & first_returns_mask)

    ratio = canopy_returns / total_first_returns if total_first_returns > 0 else 0.0

    print(f"  Canopy (first > 1.37m): {canopy_returns}, Total first: {total_first_returns}, Ratio = {ratio:.4f}")

    results.append({
        "tile": file.name,
        "canopy_first_returns": canopy_returns,
        "total_first_returns": total_first_returns,
        "canopy_cover_ratio_dbh": round(ratio, 4)
    })

# Save to CSV
df = pd.DataFrame(results)
df.to_csv(output_csv, index=False)
print(f"✅ DBH-standard canopy cover metrics saved to {output_csv}")
