#TODO: Implementar as estatísticas de comparação

import serial
import cv2
import numpy as np
from bitstring import ConstBitStream
import VLC
'''
ser = serial.Serial(
        port='/dev/ttyUSB0',
        baudrate = 100e3,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

data = ser.read()

'''
received_bits = ConstBitStream(filename='img_bits_encoded.bin').bin
n = 10 # chunk length
received_chunks = [received_bits[i:i+n] for i in range(0, len(received_bits), n)]

decoded = VLC.decArray8b10b(received_chunks)
img = cv2.imdecode(np.frombuffer(decoded, np.uint8), -1)
cv2.imwrite('macaquito.tiff', img)