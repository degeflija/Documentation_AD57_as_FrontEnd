#!/user/bin/env python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from docutils.nodes import description

file = "211001.f100"

elements = [
"acc x", "acc y", "acc z", "gyro x", "gyro y", "gyro z", "mag x", "mag y", "mag z",
"LC acc x", "LC acc y", "LC acc z", "LC gyro x", "LC gyro y", "LC gyro z", "LC mag x", "LC mag y", "LC mag z",
"pitot", "static p2", "abs p", "temp", "abs sens t", "ubatt",
"pos N", "pos E", "pos DWN", "vel N", "vel E", "vel DWN", "acc N", "acc E", "acc DWN", "track GNSS", "speed GNSS",
"relpos N", "relpos E", "relpos D", "rel HDG", "speed acc", "Lat 1", "Lat 2", "Long 1", "Long 2","ymdh", "minsec sep",
"IAS", "TAS",
"vario uncomp", "vario", "vario pressure", "speed comp TAS", "speed comp INS",
"vario integrator", "wind N", "wind E", "wind D",
"wind avg N", "wind avg E", "wind avg D",
"circle mode",
"nav acc N", "nav acc E", "nav acc D", "nav ind N", "nav ind E", "nav ind D", "nav corr N", "nav corr E", "nav corr D",
"gyro corr F", "gyro corr R", "gyro corr D", "q0",
"q1", "q2", "q3",
"roll", "nick", "yaw",
"acc vertical", "turn rate", "slip angle", "nick angle",
"navv acc mag N", "nav acc mag E", "nav acc mag D", "nav ind mag N", "nav ind mag E", "nav ind mag D",
"roll mag", "nick mag", "yaw mag", "q1mag", "q2mag", "q3mag", "q4mag", "Probe 0", "Probe 1", "Probe 2" ]

# Create a data description for the raw data file format. Assume 32 bit float for each value.
description = []
for i in range(0,100):
    description.append((elements[i], 'f4'))

# Create a pandas dataframe
dt = np.dtype(description)
data = np.fromfile(file, dtype=dt, sep="")
df = pd.DataFrame(data)

# Generate x axis in minutes
stepsize = 0.01 / 60.0  #10ms
stepcnt = len(df)
minute_list = []
print(stepsize, stepcnt)
for i in range(0,stepcnt):
    minute_list.append(i*stepsize)

# process some data
wind_speed = np.sqrt(df["wind N"] * df["wind N"] + df["wind E"] * df["wind E"])
wind_direction = np.arctan2(df["wind E"], df["wind N"])
wind_direction_deg = np.rad2deg(wind_direction) + 180
heading_deg = np.rad2deg(df["yaw"]) + 180
relative_wind = np.mod(heading_deg - wind_direction_deg, 360)

# plot the data
plt.figure(0)

fig, host = plt.subplots(figsize=(8,5)) # (width, height) in inches

par1 = host.twinx()
par2 = host.twinx()
par3 = host.twinx()
#par4 = host.twinx()
#par5 = host.twinx()

host.set_xlabel("Time in 100 Ticks / s")

host.plot(- df["pos DWN"], color='red', label="height", linestyle='dashed', linewidth=0.5)
host.set_ylabel("height [m]", color='red')

par1.plot(wind_speed, color='green', label="wind speed", linewidth=1)
par1.set_ylabel("wind speed [m/s]", color='green')
par1.set_ylim(4, 30)

par2.plot(df["turn rate"], color='orange', label="turn rate", linewidth=1)
par2.set_ylabel("turn rate [rad/s]", color='orange')
par2.set_ylim(-1, +1)

par3.plot(wind_direction_deg, color='blue', label="wind direction", linewidth=1)
par3.set_ylabel("wind direction [deg]", color='blue')

#par4.plot(heading_deg, color='magenta', label="heading", linestyle='dotted', linewidth=1)
#par4.set_ylabel("heading [deg]", color='magenta')

#par5.plot(relative_wind, color='yellow', label="relative wind", linewidth = 1)
#par5.set_ylabel("relative wind [deg]", color="yellow")


par2.spines['right'].set_position(('outward', 60))
par3.spines['right'].set_position(('outward', 120))
#par4.spines['right'].set_position(('outward', 180))
#par5.spines['right'].set_position(('outward', 240))
fig.tight_layout()

plt.figure(0)
plt.plot(df["vario"])

plt.show()


