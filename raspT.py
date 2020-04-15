#import RPi.GPIO as GPIO
from encoder import encByte8b10b, encArray8b10b
import serial
from bitstring import Bits
import time
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

with open(path, "rb") as f:
    img_bytes = f.read()

names, bits, current_disparity = encArray8b10b(img_bytes, current_disparity=-1)

def createPackage(data, length):
    return Bits().join(Bits(uint=x, length=length) for x in data) 

names, bits, current_disparity = encArray8b10b(img_bytes, current_disparity=-1)

img_bits_encoded = createPackage(bits, 10)


#ser.write(img_bytes)
