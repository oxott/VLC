#Código do para ser usado na Raspberry transmissora

#TODO: Testar a comunicação serial na Rasp

#Biblioteca para o controles dos pinos GPIO
#import RPi.GPIO as GPIO
#Biblioteca onde estão as funções para codificação de um único byte e de um array de bytes em 8b10b
from encoder import encByte8b10b, encArray8b10b, createPackage
#Biblioteca para comunicação Serial
import serial
#Biblioteca para manipulação de bits
from bitstring import Bits

#Configurações para comunicação Serial
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
#Carrega o caminho para a imagem a ser transmitida
path = "baboon.tiff"

#Lê os bytes da imagem a ser transmitida
with open(path, "rb") as f:
    img_bytes = f.read()

#Codifica o conjunto de bytes da imagem em 8b10b e gera a lista de codificações criada, os bits codificados e a paridade atual após a codificação,
#utilizando a paridade inicial como -1
names, bits, current_disparity = encArray8b10b(img_bytes, current_disparity=-1)

#Cria o pacote de bits a ser transmitido
img_bits_encoded = createPackage(bits, 10)

#Envia pela porta serial os bits
#ser.write(bits)
