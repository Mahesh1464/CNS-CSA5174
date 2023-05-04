# -*- coding: utf-8 -*-
"""
Created on Thu May  4 10:09:16 2023

@author: sridh
"""
ciphertext = "53‡‡†305))6*;4826)4‡.)4‡);806*;48†8¶60))85;;]8*;:‡8†83 (88)5†;46(;88*96*?;8)‡(;485);5†2:‡(;4956*2(5—4)8¶8* ;4069285);)6†8)4‡‡;1(‡9;48081;8:8‡1;48†85;4)485†528806*81 (‡9;48;(88;4(‡?34;48)4‡;161;:188;‡?;"
mapping = {
    "‡": "a",
    "†": "e",
    "¶": "i",
    "(": "l",
    ")": "m",
    "*": "n",
    ";": "o",
    ":": "r",
    "]": "s",
    "[": "t",
    "5": "h",
    "4": "s",
    "6": "t",
    "8": "w",
    "0": " "
}

plaintext = ""
for char in ciphertext:
    if char in mapping:
        plaintext += mapping[char]
    else:
        plaintext += char

print(plaintext)