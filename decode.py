from wav import WaveStruct
import math

with open("test_hidden.wav", "rb") as f:
    wav_bytes = f.read()

wav_parsed = WaveStruct.parse(wav_bytes)
data = wav_parsed.data_sub_chunk.data

def read_hidden_byte(offset, data):
    byte = 0
    shift = 0
    for i in range(4):
        byte = byte | ((data[offset + i] & 3) << shift)
        shift += 2
    return (byte, 4)

offset = 0
size = 0
shift = 0

for i in range(4):
    (byte, inc) = read_hidden_byte(offset, data)
    size |= size | (byte << shift)
    shift += 8
    offset += inc

print(f"Hidden file size: {size}")

hidden_data = bytearray()

for i in range(size):
    (byte, inc) = read_hidden_byte(offset, data)
    hidden_data.append(byte)
    offset += inc

with open("parrot_hidden.jpg", "wb") as f:
    f.write(hidden_data)
