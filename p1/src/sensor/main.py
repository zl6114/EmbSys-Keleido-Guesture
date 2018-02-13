from adafruit import Keleido
from lis3dh import LIS3DH
import time

# magic = Keleido(wifiName="EEERover", wifiPasswd="exhibition", topic="keleido/flex", BrokerIP = "192.168.0.10")
scl = 0
sda = 16
Lis3dh = LIS3DH(scl,sda)

while 1:
    x,y,z = Lis3dh.acceleration()
    print('x = {}G, y = {}G, z = {}G'.format(x, y, z))
    time.sleep(0.3)