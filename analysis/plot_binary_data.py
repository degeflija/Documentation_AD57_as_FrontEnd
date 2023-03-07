#!/user/bin/env python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objs as go


elements_f105 = ['acc x', 'acc y', 'acc z', 'gyro x', 'gyro y', 'gyro z', 'mag x', 'mag y', 'mag z', 'pitot',
                 'static p', 'temp', 'ubatt', 'pos N', 'pos E', 'pos DWN', 'vel N', 'vel E', 'vel DWN', 'acc N',
                 'acc E', 'acc DWN', 'track GNSS', 'speed GNSS', 'relpos N', 'relpos E', 'relpos D', 'rel HDG',
                 'speed acc', 'Lat 1', 'Lat 2', 'Long 1', 'Long 2', 'ymdh', 'minsec sat fixtype', 'nano',
                 'geo_sep+dummy', 'IAS', 'TAS', 'vario uncomp', 'vario', 'vario pressure', 'speed comp TAS',
                 'speed comp INS', 'vario integrator', 'wind N', 'wind E', 'wind D', 'wind avg N', 'wind avg E',
                 'wind avg D', 'circle mode', 'nav acc N', 'nav acc E', 'nav acc D', 'nav ind N', 'nav ind E',
                 'nav ind D', 'nav corr N', 'nav corr E', 'nav corr D', 'gyro corr F', 'gyro corr R', 'gyro corr D',
                 'q0', 'q1', 'q2', 'q3', 'roll', 'nick ', 'yaw', 'acc vertical', 'turn rate', 'slip angle',
                 'nick angle', 'G_load', 'nav acc mag N', 'nav acc mag E', 'nav acc mag D', 'nav ind mag N',
                 'nav ind mag E', 'nav ind mag D', 'roll mag', 'nick mag', 'yaw mag', 'q1mag', 'q2mag', 'q3mag',
                 'q4mag', 'acc_F', 'acc_R', 'acc_D', 'gyro_F', 'gyro_R', 'gyro_D', 'press_alt', 'SAT-MAG Hdg',
                 'QFF', 'Density', 'satfix', 'headwiind', 'crosswind', 'wind_N', 'wind_E', 'mag_disturbance']


# Put the file name you want to use here:
file = "flug.f37.f105"

if file.endswith('.f105'):
    elements = elements_f105
else:
    print('Format, not supported')
    exit()


# Create a data description for the raw data file format. Assume 32 bit float for each value.
description = []
for i in range(0, len(elements)):
    description.append((elements[i], 'f4'))

# Create a pandas dataframe
dt = np.dtype(description)
data = np.fromfile(file, dtype=dt, sep="")
df = pd.DataFrame(data)

# Skip the data not flying:
df = df[150000:]

# Prepare the data
windDirectionAvg = np.arctan2( - df['wind avg E'], - df['wind avg N']) / 2 / np.pi * 360
windDirectionInst = np.arctan2( - df['wind E'], - df['wind N']) / 2 / np.pi * 360
windSpeedAvg = np.sqrt(np.square(df['wind avg E']) + np.square(df['wind avg N'])) * 3.6
windSpeedInst = np.sqrt(np.square(df['wind E']) + np.square(df['wind N'])) * 3.6
heading = df['yaw'] / 2 / np.pi * 360

# Plot the data:
figure, axis = plt.subplots(2, 2, sharex=True)
plt.autoscale(enable=True, axis='y')
axis[0, 0].plot(windDirectionAvg, "b-", label='Average', alpha=0.4)
axis[0, 0].plot(windDirectionInst, "b--", label='Instantaneous', alpha=0.4,)

par1 = axis[0, 0].twinx()
par1.plot(windSpeedAvg, "r-", label='Average', alpha=0.4)
par1.plot(windSpeedInst, "r--", label='Instantaneous', alpha=0.4)

axis[0, 0].legend(["average wind direction", "inst wind direction"], loc="lower left")
par1.legend(["average wind speed", "inst wind speed"], loc="lower right")

axis[1, 0].plot(df['turn rate'], "b--", alpha=0.4 )
axis[1, 0].legend(["turn rate"], loc="lower left")
par1 = axis[1, 0].twinx()
par1.plot(df['circle mode'], "y-")
par1.legend(["circle mode"], loc="lower right")


axis[0, 1].plot(df['press_alt'], "b--", alpha=0.4 )
axis[0, 1].legend(["pressure altitude"], loc="lower left")


axis[1, 1].plot(df['vario'], "b-", alpha=0.4 )
axis[1, 1].legend(["vario"], loc="lower left")

plt.show()



