
import geopandas as gpd
from shapely.geometry import box
from pathlib import Path

# Settings
input_dir = Path("data/normalized_las_100m")
output_path = "data/tiles_100m.shp"
tile_size = 100  # meters
crs_epsg = 32651  # UTM Zone 51N

records = []

for file in input_dir.glob("tile_*.las"):
    try:
        parts = file.stem.split("_")
        x = int(parts[1])
        y = int(parts[2])
        geom = box(x, y, x + tile_size, y + tile_size)
        records.append({"tile": file.name, "geometry": geom})
    except Exception as e:
        print(f"Skipping {file.name}: {e}")

gdf = gpd.GeoDataFrame(records, crs=f"EPSG:{crs_epsg}")
gdf.to_file(output_path)

print(f"✅ Shapefile created: {output_path}")
