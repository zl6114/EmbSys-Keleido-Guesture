from machine import Pin, I2C

i2c = I2C(scl=Pin(4), sda=Pin(5), freq=100000)
i2cportNo = i2c.scan()

print(i2cportNo)
