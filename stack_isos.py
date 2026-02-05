import geopandas as gpd
from pathlib import Path
import pandas as pd
from datetime import datetime 

ISO_DIR = Path("isochrones")
OUT_FILE = Path("isochrones_stacked.geojson")

gdfs = []

# Sort files by numeric time suffix
files = sorted(
    ISO_DIR.glob("*.geojson"),
    key=lambda f: int(f.stem.split("_")[-1])
)

for f in files:
    gdf = gpd.read_file(f)

    time_str = f.stem.split("_")[-1]

    # Add back datetime. Whoops. 
    time = datetime(2025, 12, 16, int(time_str))
    gdf["time_of_day"] = time

    gdfs.append(gdf)

stacked = gpd.GeoDataFrame(
    pd.concat(gdfs, ignore_index=True),
    crs=gdfs[0].crs
)

stacked.to_file(OUT_FILE, driver="GeoJSON")

print(f"Saved stacked isochrones to {OUT_FILE}")
