
import os
import laspy
import numpy as np
import pandas as pd
from pathlib import Path

# Paths
input_dir = Path("data/normalized_las_100m")
output_csv = Path("data/voxel_cover_metrics_100m.csv")

# Parameters
voxel_size = 1.0
min_height = 0.5
max_height = 3.5

results = []

for file in input_dir.glob("*.las"):
    print(f"Processing {file.name}...")
    las = laspy.read(file)
    x, y, z = las.x, las.y, las.z

    # Filter for understory range
    mask = (z >= min_height) & (z <= max_height)
    x, y, z = x[mask], y[mask], z[mask]

    print(f"  Total points: {len(z)} in understory range ({min_height}-{max_height}m)")

    if len(z) == 0:
        print("  ⚠️ No points in understory range.")
        voxel_count = 0
        total_voxels = 0
        density = 0.0
    else:
        x_idx = np.floor(x / voxel_size).astype(int)
        y_idx = np.floor(y / voxel_size).astype(int)
        z_idx = np.floor(z / voxel_size).astype(int)

        voxel_ids = set(zip(x_idx, y_idx, z_idx))

        voxel_count = len(voxel_ids)
        total_voxels = (np.ptp(x_idx) + 1) * (np.ptp(y_idx) + 1) * (np.ptp(z_idx) + 1)
        density = voxel_count / total_voxels if total_voxels > 0 else 0

        print(f"  ✅ {voxel_count} occupied voxels / {total_voxels} total → ratio = {density:.4f}")

    results.append({
        "tile": file.name,
        "occupied_voxels": voxel_count,
        "total_voxels": total_voxels,
        "voxel_occupancy_ratio": round(density, 4)
    })

# Save to CSV
df = pd.DataFrame(results)
df.to_csv(output_csv, index=False)
print(f"✅ Results saved to {output_csv}")
