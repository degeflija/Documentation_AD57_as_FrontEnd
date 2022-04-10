# Overview
Project description: https://github.com/larus-breeze/documentation_and_utilities/blob/master/documentation/Manuals/HKM_VM_Overview.pdf

![Systemoverview](documentation/CAN_bus_cable_schema.drawio.png)

## How to Build 

### Components and Software
#### Frontend 
- Display and user interface
- https://github.com/larus-breeze/sw_frontend

#### Central Unit  / central sensor
- Processing of all sensor signals and computation of vario signal
- https://github.com/larus-breeze/hw_sensor
- https://github.com/larus-breeze/sw_sensor

#### Utility module    
- Blue pill or F4 based utility module to generate the vario audio sound. Can additionally sense temperature and humidity. 
- https://github.com/larus-breeze/hw_utility
- https://github.com/larus-breeze/sw_utility

#### Sense module for temperature and humidity
- Optional small sense module to measure temperature and humidity
- https://github.com/larus-breeze/hw_sense



### TODO:
- add a hardware overview picture with the CAN wiring
- 
