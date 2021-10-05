#!/user/bin/env python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

# Plot some speed GNSS data.
plt.plot(df["speed GNSS"])
plt.show()


