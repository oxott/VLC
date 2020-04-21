#Arquivo com as funções necessárias para codificação

from bitstring import Bits
import numpy as np

#Tabela de conversão 3b4b
table_3b4b = {
    0b000: (".0",   (0b0100,0b1011)),
    0b001: (".1",   (0b1001,)      ),
    0b010: (".2",   (0b0101,)      ),
    0b011: (".3",   (0b0011,0b1100)),
    0b100: (".4",   (0b0010,0b1101)),
    0b101: (".5",   (0b1010,)      ),
    0b110: (".6",   (0b0110,)      ),
    0b111: (".7",   (0b0001,0b1110, 0b1000, 0b0111)),
}

#Tabela de conversão 5b6b
table_5b6b = {
    0b00000: ("D.0",    (0b100111, 0b011000)),
    0b00001: ("D.1",    (0b011101, 0b100010)),
    0b00010: ("D.2",    (0b101101, 0b010010)),
    0b00011: ("D.3",    (0b110001,)         ),
    0b00100: ("D.4",    (0b110101, 0b001010)),
    0b00101: ("D.5",    (0b101001,)         ),
    0b00110: ("D.6",    (0b011001,)         ),
    0b00111: ("D.7",    (0b111000, 0b000111)),
    0b01000: ("D.8",    (0b111001, 0b000110)),
    0b01001: ("D.9",    (0b100101, )        ),
    0b01010: ("D.10",   (0b010101, )        ),
    0b01011: ("D.11",   (0b110100, )        ),
    0b01100: ("D.12",   (0b001101, )        ),
    0b01101: ("D.13",   (0b101100, )        ),
    0b01110: ("D.14",   (0b011100, )        ),
    0b01111: ("D.15",   (0b010111, 0b101000)),
    0b10000: ("D.16",   (0b011011, 0b100100)),
    0b10001: ("D.17",   (0b100011, )        ),
    0b10010: ("D.18",   (0b010011, )        ),
    0b10011: ("D.19",   (0b110010, )        ),
    0b10100: ("D.20",   (0b001011, )        ),
    0b10101: ("D.21",   (0b101010, )        ),
    0b10110: ("D.22",   (0b011010, )        ),
    0b10111: ("D.23",   (0b111010, 0b000101)),
    0b11000: ("D.24",   (0b110011, 0b001100)),
    0b11001: ("D.25",   (0b100110, )        ),
    0b11010: ("D.26",   (0b010110, )        ),
    0b11011: ("D.27",   (0b110110, 0b001001)),
    0b11100: ("D.28",   (0b001110, )        ),
    0b11101: ("D.29",   (0b101110, 0b010001)),
    0b11110: ("D.30",   (0b011110, 0b100001)),
    0b11111: ("D.31",   (0b101011, 0b010100)),
}

#Função para extrair da tabela o código referente ao data e atualizar a disparidade
def getCode(table, data, disparity = 0):
    name, encodings = table[data]
    
    if disparity < 0:
        encoding = encodings[-1]
        disparity +=1 if len(encodings) > 1 else 0
    else:
        encoding = encodings[0]
        disparity -=1 if len(encodings) > 1 else 0

    return name, encoding, disparity

#Função para concatenar os códigos extraidos da tabela e finalizar a codificação 8b10b
def encByte8b10b(byte, current_disparity=0, verbose=False):
    if verbose:
        print(f'Input Disparity = {current_disparity}')
    p1 = (byte>>5)&(0b111)
    p2 = (byte)&(0b00011111)

    name_2, abcdei, _ = getCode(table_5b6b, p2, current_disparity)
    name_1, fghj, current_disparity = getCode(table_3b4b, p1, current_disparity)

    encoded = (fghj | abcdei<<4)

    if verbose:
        print(f'{byte} = {byte:#010b} = {p1:#05b} {p2:#07b}')
        print(f'{p2:#07b} = {name_2} = {abcdei:#08b}, {p1:#05b} = {name_1} = {fghj:#06b}')
        print(f'encoded {encoded} = {encoded:#012b}')
        print(f'Output Disparity = {current_disparity}\n')

    return encoded, name_2+name_1, current_disparity

#Função para codificar array de bytes
def encArray8b10b(array, current_disparity = 0):
    names = []
    bits = []
    for byte in array:
        code, name, current_disparity = encByte8b10b(byte, current_disparity)
        names.append(name)
        bits.append(code)
    return (names, bits, current_disparity)

#Cria um conjunto com os bits a serem transmitidos
def createPackage(data, length):
    return Bits().join(Bits(uint=x, length=length) for x in data) 

def decCode(table, code_bits):
    for bits, (_, mapped_bits) in table.items():
        if code_bits in mapped_bits:
            return bits

def decByte8b10b(code_bits):
    bits1 = decCode(table_5b6b, ((code_bits>>4) & 0b111111))
    bits2 = decCode(table_3b4b, ((code_bits>>0) & 0b1111))
    return (bits2<<5) | bits1

def decArray8b10b(code_array):
    bits = np.zeros((len(code_array),), dtype='uint8')
    for i, code in enumerate(code_array):
        bits[i] = decByte8b10b(int(code, 2))
    return bits

