#TODO: Testar a comunicação serial na Rasp

from encoder import encByte8b10b, encArray8b10b, createPackage
import serial
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

with open(path, "rb") as f:
    img_bytes = f.read()

names, bits, current_disparity = encArray8b10b(img_bytes, current_disparity=-1)

img_bits_encoded = createPackage(bits, 10)

#ser.write(bits)
