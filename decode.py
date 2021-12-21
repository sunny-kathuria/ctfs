import sys

morse_table = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    " ": " ",
    "\n": ""
}

trinity_table = {
    ".": "0",
    "-": "1",
    " ": "2"
}

def morse_encode(s):
    return ' '.join([ morse_table[c] for c in s ])

def trinity_encode(s):
    return ''.join([ trinity_table[c] for c in morse_encode(s) ])

#cipher_output = "1202010210201201021011200200021121112010202012010210102012102021000200121200210002021210112111200121200002111200121102000021211120010200212001020020102000212"
a="TERNARYISMOREARCANEBUTIBETYOUTHOUGHTOFITFIRST"
plaintext=a.lower()
print(plaintext)
ciphertext = trinity_encode(plaintext)
print(ciphertext)





#decode

def decode(s):
   decoded=""
   for i in cipher_output:
      temp=list(trinity_table.keys())[list(trinity_table.values()).index(i)]
      decoded=decoded+temp
   return decoded


#decode()
#print(abc)




