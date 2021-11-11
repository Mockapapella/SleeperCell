from pathlib import Path

filename = Path("exploit.py")
with open(filename, "r+", encoding="utf8") as file:
    file = file.read()
print("#" * 40 + " FILE CONTENTS " + 40 * "#")
print(file)

dictionary = {"0": "0000",
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
            "f": "1111"}

command = file.encode().hex()

command = [command[i : i + 2] for i in range(0, len(command), 2)]
print("#" * 40 + " EACH CHARACTER CONVERTED TO HEX " + 40 * "#")
print(command)
hex_string = ""
binary_string = ""
for hexadec in command:
    hex_string += hexadec
for hexadec in hex_string:
    binary_string += dictionary[hexadec]
print(binary_string)

command = "\\x" + "\\x".join(command)
print("#" * 40 + " CONVERTED TO BYTESTRING " + 40 * "#")
print(command)
print(type(command))

command = command.encode("ascii").decode("unicode-escape")
print("#" * 40 + " EXECUTE BYTESTRING " + 40 * "#")
exec(command)
