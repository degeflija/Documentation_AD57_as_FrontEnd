# Overview

https://github.com/larus-breeze/documentation_and_utilities/blob/master/documentation/Manuals/HKM_VM_Overview.pdf


![ystemoverview](documentation/CAN_bus_cable_schema.drawio.png)

## How to Build 

### Hardware Parts and PCB
#### Frontend 
- Display and user interface
#### Central Unit 
- Processing of all sensor signals and computation of vario signal
- https://github.com/larus-breeze/hw_instrument
- https://github.com/larus-breeze/sw_instrument

#### Audio module
- Blue pill based audio module to generate audio sound. 
- https://github.com/larus-breeze/hw_audio
- https://github.com/larus-breeze/sw_audio

#### external Sensor (temperature, humidity)
- optional sensor to measure temperature and humidity
- https://github.com/larus-breeze/hw_sense

### Software
- Build & Flash