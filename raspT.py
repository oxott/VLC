#TODO: Testar a comunicação serial na Rasp

import encoder
import numpy as np
import serial
import sys
from bitstring import Bits


'''
#Configura o uso do terminal serial e da taxa de transmissão de dados
ser = serial.Serial(
    port='/dev/ttyS0',
    baudrate = 100e3,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)
'''
path = "baboon.tiff"
'''
with open(path, "rb") as f:
    img_bytes = f.read()
'''
img_bytes = np.fromfile(path, dtype='uint8')  

names, bits, current_disparity = VLC.encArray8b10b(img_bytes, current_disparity=-1)
img_bits_encoded = VLC.createPackage(bits, 10)

with open('img_bits_encoded.bin', 'wb') as f:
    img_bits_encoded.tofile(f)

#ser.write(bits)
