from gtfslite import GTFS

data = GTFS.load_zip("GTFS/MIR-Train-GTFS.zip")
print(data.summary())