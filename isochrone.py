import r5py
from shapely.geometry import Point
from datetime import datetime

# Setup network, etc. 
transport_network = r5py.TransportNetwork(
    "kanto.pbf",
    ["GTFS/Toei-Train-GTFS.zip", 
     "GTFS/TokyoMetro-Train-GTFS.zip",
     "GTFS/MIR-Train-GTFS.zip"]
)

bancho = Point(139.7354183, 35.6865515)

def make_isochrone(date: datetime):
    print(f"Making isochrome for date {date}")
    isochrones = r5py.Isochrones(
        transport_network,
        origins=bancho,
        departure= date,
        transport_modes=[r5py.TransportMode.TRANSIT, r5py.TransportMode.WALK],
        isochrones=[15,30,45],
    )

    # Save file
    isochrones = isochrones.copy()
    for col in isochrones.columns:
        if str(isochrones[col].dtype).startswith("timedelta"):
            isochrones[col] = (
                isochrones[col].dt.total_seconds() / 60
            )
    path = f"isochrones/isochrone_{date.hour}.geojson"
    isochrones.to_file(path, driver="GeoJSON")

# Iterate through times 
for i in range(0,24,2):
    date = datetime(2025, 12, 16, 1+i)
    make_isochrone(date)