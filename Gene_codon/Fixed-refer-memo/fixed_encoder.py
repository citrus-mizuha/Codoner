import json
import random

# 固定のコドン表の定義
codon_table = {
    0: ["000", "001", "002", "003"],
    1: ["010", "011", "012", "013"],
    2: ["020", "021", "022", "023"],
    3: ["030", "031", "032", "033"],
    4: ["100", "101", "102", "103"],
    5: ["110", "111", "112", "113"],
    6: ["120", "121", "122", "123"],
    7: ["130", "131", "132", "133"],
    8: ["200", "201", "202", "203"],
    9: ["210", "211", "212", "213"],
    10: ["220", "221", "222", "223"],
    11: ["230", "231", "232"],
    12: ["233", "300", "301"],
    13: ["302", "303", "310"],
    14: ["311", "312", "313"],
    15: ["320", "321", "322"],
    "S": ["323"],
    "F": ["330", "331", "332", "333"]
}

input_string = input("文字列 : ")

def string_to_binary(input_string):
    utf8_bytes = input_string.encode('utf-8')
    binary_string = ''.join(format(byte, '08b') for byte in utf8_bytes)
    return binary_string

def split_into_chunks(binary_string):
    chunks = [binary_string[i:i+4] for i in range(0, len(binary_string), 4)]
    return chunks

def encrypt_data(chunks):
    encrypted_data = []
    for chunk in chunks:
        value = int(chunk, 2)
        if value in codon_table:
            codon_choices = codon_table[value]
            chosen_codon = random.choice(codon_choices)
            encrypted_data.append(chosen_codon)
        else:
            encrypted_data.append("Invalid")
    encrypted_data.insert(0, "323")
    encrypted_data.append(random.choice(["330", "331", "332", "333"]))
    return encrypted_data

def convert_to_binary(encrypted_data):
    binary_string = ''.join(codon for codon in encrypted_data)
    return binary_string

utf8_binary = string_to_binary(input_string)
print("UTF-8 Binary:", utf8_binary)
binary_chunks = split_into_chunks(utf8_binary)
print("Binary Chunks:", binary_chunks)
encrypted_data = encrypt_data(binary_chunks)
print("Pseudo-Quaternary:", encrypted_data)
converted_binary = convert_to_binary(encrypted_data)
print("Converted Binary:", converted_binary)