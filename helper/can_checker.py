from can.interfaces.seeedstudio.seeedstudio import SeeedBus
import threading
from collections import deque
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from datetime import datetime



class CanGet(threading.Thread):
    temperature = 0.0
    humidity = 0.0
    pressure = 0.0

    tas = 0.0
    ias = 0.0
    static_pressure = 0.0

    stop = False
    file = None

    def __init__(self, channel):
        super(CanGet, self).__init__()
        self.bus = SeeedBus(bustype='seeedstudio', channel=channel, bitrate=1000000)
        filename = datetime.utcnow().strftime("%Y%m%d%H%M%S") + '_data.csv'
        self.file = open(filename, 'w')
        self.file.writelines(["Time,Temperature,Humidity,Pressure\n"]) # Write header

    def run(self):
        while True:
            rxMessage = self.bus.recv()
            if rxMessage is not None:
                if rxMessage.arbitration_id == 0x214:
                    self.temperature = (int.from_bytes(rxMessage.data, 'little', signed="True")) / 1000.0

                if rxMessage.arbitration_id == 0x215:
                    self.humidity = (int.from_bytes(rxMessage.data, 'little', signed="False")) / 1000.0

                if rxMessage.arbitration_id == 0x216:
                    self.pressure = (int.from_bytes(rxMessage.data, 'little', signed="False")) / 1000.0

                if rxMessage.arbitration_id == 0x216:
                    line = '{},{},{},{}\n'.format(datetime.utcnow().strftime("%Y%m%d%H%M%S%f"), self.temperature, self.humidity, self.pressure)
                    print(line, end="")
                    self.file.writelines([line])
                    self.file.flush()

                if rxMessage.arbitration_id == 0x102:  # Airspeed
                    self.tas = (int.from_bytes(rxMessage.data[0:1], 'little', signed="False"))
                    self.ias = (int.from_bytes(rxMessage.data[2:3], 'little', signed="False"))
                    print("TAS: ", self.tas, " IAS: ", self.ias)


                if rxMessage.arbitration_id == 0x109:  # Atmosphere
                    pass
                    #print("Atmosphere", rxMessage.data)




            if self.stop is True:
                try:
                    self.file.close()
                except Exception as e:
                    print(e)
                return

    def stop(self):
        self.stop = True


interface = CanGet('COM20')
interface.start()



