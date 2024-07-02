#!/usr/bin/env python3
# author: Jelena
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import rc

# mpl setup
font_size = 15
mpl.rcParams["lines.markersize"] = 5
rc("font", **{"family": "serif", "serif": ["Palatino"], "size": font_size})
rc("text", usetex=True)

path = "GP13_true.txt"
df = pd.read_csv(path, delimiter=",")

x = df["GPS Longitude (deg)"]
y = df["GPS Latitude (deg)"]
z = df["GPS Altitude (m)"]


plt.title("Absolute Positions of DUs")
plt.scatter(x, y, color = "hotpink")
# Add labels for each point (DU ID)
for i, row in df.iterrows():
    du_id = row["DU"]
    plt.annotate(int(du_id - 1000), (x[i], y[i]))
plt.xlabel("GPS Longitude (deg)")
plt.ylabel("GPS Latitude (deg)")
plt.tight_layout()
plt.savefig("GP13_GPS_2D.png", dpi = 300)
plt.close()

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
plt.title("Absolute Positions of DUs")
ax.scatter(x, y, z, color="hotpink")
ax.set_xlabel("GPS Longitude (deg)")
ax.set_ylabel("GPS Latitude (deg)")
ax.set_zlabel("GPS Altitude (m)")
plt.tight_layout()
plt.savefig("GP13_GPS_3D.png", dpi = 300)
plt.show()
plt.close()
