import string
from textwrap import wrap

asciiChar = [chr(i).encode("ascii") for i in range(0, 128)]


# Shift char in message by pos
def ROT(message, pos, alphabet=list(string.printable)):
    rot13_enc = ''
    for c in message:
        i = alphabet.index(c)
        rot13_enc += alphabet[(i+pos) % len(alphabet)]
    return rot13_enc


# XOR the message with the given key
def XOR(message, KEY):
    rep = len(message)//len(KEY) + 1
    key = (KEY*rep)[:len(message)] # adjust the key len
    xored = ''.join([chr(ord(a) ^ ord(b)) for a,b in zip(message, key)])
    return xored


# Convert string with only 0 and 1 to the corrisponding string
# if there is a separator between bytes specify it
def binToStr(binStr: str, separator: str =None):
    if separator == None:
        binStr = wrap(binStr, 7)
    else:
        binStr = binStr.split(separator)
    message = ""
    for char in binStr:
        message += chr(int(char, 2))
    return message


# Replace all char in message with the corrisponding specified in charList
def replacer(message: str, charList: dict):
    msg = message
    for key in charList:
        msg = msg.replace(key, charList[key])
    return msg
