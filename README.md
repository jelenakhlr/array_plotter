This repository contains two Python scripts for plotting antenna positions from GNSS data files.

# Scripts
## Plot Antenna Array in GPS coordinates

This script plots antenna positions directly from a specified file in  GPS coordinates (degrees).  

`python plot_GPS.py`

*Note:* The file path is currently hardcoded in the script.

## Plot Antenna Array in meters

This script plots antenna positions in meters relative to an origin point. 

It first converts the GPS coordinates (degrees) from the data file to relative meters, then plots them.

`python plot_meters_from_GPS.py`

*Note:*
    
    1. The file path is currently hardcoded in the script. 
    
    2. The origin point is currently hardcoded in the script.


# Output

Both scripts will generate a plots in both 2D and 3D showing the given antenna positions.

# Additional Notes

This is a basic implementation for example use and can be further customized for specific needs.