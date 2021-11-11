from pathlib import Path

encoded_message = ""
filename = Path("main.py")
with open(filename, "r+", encoding="utf8") as file:
    file = file.read()
    for character in file:
        encoded_message += character
        if encoded_message.endswith("AAAAAAAA"):
            encoded_message = encoded_message[-8:]
        if encoded_message.endswith("BBBBBBBB"):
            break

# change every instance of A to 1 and B to 0
for character in encoded_message:
    if character == "A":
        encoded_message = encoded_message.replace(character, "1")
    else:
        encoded_message = encoded_message.replace(character, "0")

some_string = ""
n=8
encoded_message = encoded_message[8:-8]
encoded_message = [hex(int(encoded_message[i:i+n], 2)) for i in range(0, len(encoded_message), n)]
for x in encoded_message:
    some_string += "\\x" + x[2:]
some_string = some_string.encode("ascii").decode("unicode-escape")


# print(type(some_string))
exec(some_string)
# for number, hexadec in enumerate(encoded_message):
#     bytestring =
#     encoded_message[number] = f"\\x{}"
# print(encoded_message)