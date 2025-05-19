
# Taal LiDAR Understory Mapping – Final Workflow

This project assesses the potential of NDVI to reflect forest structural metrics derived from LiDAR, with a focus on understory complexity. The workflow spans from raw `.laz` files to full metric comparison and regression analysis.

---

## 🧱 Folder Structure

```
TAAL-LIDAR-UNDERSTORY/
├── data/
│   ├── normalized_las_100m/
│   ├── ndvi_mar_may_2017.tif
│   ├── tiles_100m.shp
│   ├── voxel_cover_metrics_100m.csv
│   ├── fractional_cover_metrics_100m.csv
│   ├── normalized_cover_metrics_100m.csv
│   ├── lad_metrics_100m.csv
│   ├── canopy_cover_metrics_dbh_100m.csv
│   ├── all_metrics_100m.csv
│   ├── ndvi_tile_stats_2017.csv
│   ├── all_metrics_with_ndvi_100m.csv
│   └── plots/
├── scripts/
│   └── [processing + plotting scripts]
└── README.md
```

---

## 🔧 LiDAR Preprocessing (LAStools)

1. **Merge .laz tiles**
2. **Tile into 100m × 100m grids**
3. **Classify ground points**
4. **Normalize height**
5. **Convert to .las format**

---

## 📊 LiDAR Metrics Computed (Python)

- **Voxel Cover**
- **Fractional Cover**
- **Normalized Cover**
- **Leaf Area Density (LAD)**
- **Canopy Cover (DBH > 1.37m)**

Each metric was computed tile-by-tile and saved as individual CSVs, then merged into `all_metrics_100m.csv`.

---

## 🛰️ NDVI Acquisition and Integration

- Downloaded March–May 2017 NDVI (Sentinel-2 TOA) via GEE
- Exported and visualized in QGIS
- Computed **zonal mean NDVI per tile**
- Joined with LiDAR metrics into `all_metrics_with_ndvi_100m.csv`

---

## 📈 Analysis and Visualization

- **Scatterplots and Correlation**: NDVI vs each LiDAR metric
- **Regression Model**: Predicted NDVI from all five LiDAR metrics
- **R² = 0.822**, confirming NDVI aligns strongly with canopy, but weakly with understory metrics

All plots and figures were saved to `data/plots/`.

---

## 🧠 Conclusion

This study demonstrates that:
- NDVI is strongly linked to **canopy structure**
- NDVI **fails to capture** detailed vertical or understory complexity
- LiDAR remains essential for structural vegetation mapping

