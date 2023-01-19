from wav import WaveStruct
import math

with open("test.wav", "rb") as f:
    wav_bytes = f.read()

wav_parsed = WaveStruct.parse(wav_bytes)
data = wav_parsed.data_sub_chunk.data

with open("parrot.jpg", "rb") as f:
    parrot_bytes = f.read()

available_space = math.floor(len(data) / 4)

print(f"Available space = {available_space}")
print(f"Bytes to store = {len(parrot_bytes)}")

if len(parrot_bytes) > available_space:
    print("Not enough space to store hidden file")
    exit(1)

def as_u16(value):
    if (value & 0x8000):
        return -((value ^ 0xffff) + 1)
    return value

def write_hidden_byte(byte, data, offset):
    for i in range(4):
        data[offset + i] = as_u16((data[offset + i] & 0xfffc) | (byte & 3))
        byte >>= 2
    return 4

offset = 0
hidden_file_size = len(parrot_bytes).to_bytes(4, 'little')
print(list(hidden_file_size))

for byte in hidden_file_size:
    offset += write_hidden_byte(byte, data, offset)

for byte in parrot_bytes:
    offset += write_hidden_byte(byte, data, offset)

with open("test_hidden.wav", "wb") as f:
    f.write(WaveStruct.build(wav_parsed))
