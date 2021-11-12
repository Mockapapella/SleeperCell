# What is this?
Sleeper Cell is an exploit that abuses zero width characters in Unicode to discretely embed full length programs in the comments of other programs or regular text files. This on its own is rather harmless, but when you use a decoder on a seemingly harmless file it allows you to run the exploit.

`exploit.py` is the malicious code you wish to hide in the victim's file
`encoder.py` is used to encode `exploit.py` into a binary string of zero width spaces (`\u200B` and `\u200C`)
`victim.py` is the victim's source code, text file, or any other filetype that allows arbitrary text to reside
`decoder.py` is used to search through the file until it finds a designated header and footer, decodes what's in between, rebuilds the binary into a bytestring, and executes the code.
