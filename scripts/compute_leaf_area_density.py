
import laspy
import numpy as np
import pandas as pd
from pathlib import Path
import math

# Input/output paths
input_dir = Path("data/normalized_las_100m")
output_csv = Path("data/lad_metrics_100m.csv")

# Binning parameters
bin_size = 1.0
max_height = 30.0
target_range = (0.5, 3.5)
k = 1  # extinction coefficient; unitless, set to 1 for relative LAD

results = []

for file in input_dir.glob("*.las"):
    print(f"Processing {file.name}...")
    las = laspy.read(file)
    z = las.z

    if len(z) == 0:
        results.append({
            "tile": file.name,
            "lad_0.5_3.5m": 0.0
        })
        continue

    # Bin heights
    bins = np.arange(0, max_height + bin_size, bin_size)
    bin_counts, _ = np.histogram(z, bins)

    # Cumulative sum from top to bottom for denominator (N_cum)
    cum_counts = np.cumsum(bin_counts[::-1])[::-1]

    lad_values = []
    for i in range(len(bin_counts)):
        N_bin = bin_counts[i]
        N_cum = cum_counts[i]

        if N_bin > 0 and N_cum > 0:
            lad = -math.log(N_bin / N_cum) / k
            lad_values.append((bins[i], lad))
        else:
            lad_values.append((bins[i], 0.0))

    # Extract LAD values in 0.5–3.5 m and compute mean
    lad_understory = [lad for height, lad in lad_values if target_range[0] <= height < target_range[1]]
    mean_lad = round(np.mean(lad_understory), 4) if lad_understory else 0.0

    results.append({
        "tile": file.name,
        "lad_0.5_3.5m": mean_lad
    })

# Save results
df = pd.DataFrame(results)
df.to_csv(output_csv, index=False)
print(f"✅ LAD metrics saved to {output_csv}")
