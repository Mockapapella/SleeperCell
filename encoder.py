from pathlib import Path
import pyperclip

HEX2BINARY = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "a": "1010",
    "b": "1011",
    "c": "1100",
    "d": "1101",
    "e": "1110",
    "f": "1111",
}
HEX_STRING = ""
BINARY_STRING = ""
HEADER = "\u200B\u200B\u200B\u200B\u200B\u200B\u200B\u200B"
FOOTER = "\u200C\u200C\u200C\u200C\u200C\u200C\u200C\u200C"
EXPLOIT_FILE = Path("exploit.py")

with open(EXPLOIT_FILE, "r+", encoding="utf8") as file:
    exploit_code = file.read().encode().hex()

for hex in exploit_code:
    BINARY_STRING += HEX2BINARY[hex]

print(BINARY_STRING)

BINARY_STRING = BINARY_STRING.replace("1", "\u200B")
BINARY_STRING = BINARY_STRING.replace("0", "\u200C")

BINARY_STRING = HEADER + BINARY_STRING + FOOTER

pyperclip.copy(BINARY_STRING)
print("The exploit has been copied to your clipboard.")
