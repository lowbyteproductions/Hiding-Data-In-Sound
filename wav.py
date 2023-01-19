from construct import *

# Define the parser
RiffChunk = Struct(
    "magic" / Const(b"RIFF"),
    "size"  / Int32ul,
    "wave"  / Const(b"WAVE")
)

FormatSubChunk = Struct(
    "id"                / Const(b"fmt "),
    "sub_chunk1_size"   / Int32ul,
    "audio_format"      / Int16ul,
    "num_channels"      / Int16ul,
    "sample_rate"       / Int32ul,
    "byte_rate"         / Int32ul,
    "block_align"       / Int16ul,
    "bits_per_sample"   / Int16ul,
)

DataSubChunk = Struct(
    "id"    / Const(b"data"),
    "size"  / Int32ul,
    "data"  / GreedyRange(Int16sl)
)

WaveStruct = Struct(
    "riff_chunk"        / RiffChunk,
    "format_sub_chunk"  / FormatSubChunk,
    "data_sub_chunk"    / DataSubChunk
)
