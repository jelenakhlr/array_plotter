#!/usr/bin/env python3
# author: Jelena
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import rc

# mpl setup
font_size = 15
mpl.rcParams["lines.markersize"] = 5
rc("font", **{"family": "serif", "serif": ["Palatino"], "size": font_size})
rc("text", usetex=True)


def convert_to_meters(origin_lon, origin_lat, path):
    earthRadius = 111132
    du_data = pd.read_csv(path, delimiter=",")
    # Select relevant columns and subtract origin coordinates
    df = du_data
    df["dX (meters)"] = (df["GPS Longitude (deg)"] - origin_lon) * earthRadius
    df["dY (meters)"] = (df["GPS Latitude (deg)"] - origin_lat) * earthRadius

    return df


# WARNING: this is hardcoded
origin_lon = 93.954108  # Longitude of origin (DU 1013)
origin_lat = 40.993696  # Latitude of origin (DU 1013)

path = "GP13_true.txt"
df = convert_to_meters(origin_lon, origin_lat, path)
print(df)


# Select columns for plotting (X and Y)
x = df["dX (meters)"]
y = df["dY (meters)"]
z = df["GPS Altitude (m)"]

# Create the plot
plt.figure(figsize=(8, 6))  # Adjust figure size as desired
plt.scatter(x, y, color="hotpink")

# Add labels for each point (DU ID)
for i, row in df.iterrows():
    du_id = row["DU"]
    plt.annotate(int(du_id - 1000), (x[i], y[i]))

# Add labels and title
plt.xlabel("x (meters)")
plt.ylabel("y (meters)")
plt.title("Relative Positions of DUs (Origin: DU 13)")
plt.grid()
plt.savefig("GP13_meters_2D.png", dpi=300)
plt.close()

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
plt.title("Relative Positions of DUs (Origin: DU 13)")
ax.scatter(x, y, z, color="hotpink")
ax.set_xlabel("GPS Longitude (deg)")
ax.set_ylabel("GPS Latitude (deg)")
ax.set_zlabel("GPS Altitude (m)")
plt.tight_layout()
plt.savefig("GP13_meters_3D.png", dpi = 300)
plt.show()
plt.close()