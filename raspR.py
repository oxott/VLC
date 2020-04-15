#Código do Receptor
#TODO: Implementar as estatísticas de comparação

import time
import serial
import cv2
import numpy as np

ser = serial.Serial(
        port='/dev/ttyUSB0',
        baudrate = 100e3,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

#Lê os bits enviados pela entrada serial
data = ser.read()

#decodifica a imagem recebida pela serial
decoded = cv2.imdecode(np.frombuffer(data, np.uint8), -1)
