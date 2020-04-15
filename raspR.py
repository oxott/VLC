import time
import serial
import cv

ser = serial.Serial(
        port='/dev/ttyUSB0',
        baudrate = 100e3,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

data = ser.read()

decoded = cv2.imdecode(np.frombuffer(data, np.uint8), -1)
