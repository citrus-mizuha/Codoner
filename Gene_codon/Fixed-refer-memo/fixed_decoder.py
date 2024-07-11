codon_table_to_decode = {
    "000": 0,
    "001": 0,
    "002": 0,
    "003": 0,
    "010": 1,
    "011": 1,
    "012": 1,
    "013": 1,
    "020": 2,
    "021": 2,
    "022": 2,
    "023": 2,
    "030": 3,
    "031": 3,
    "032": 3,
    "033": 3,
    "100": 4,
    "101": 4,
    "102": 4,
    "103": 4,
    "110": 5,
    "111": 5,
    "112": 5,
    "113": 5,
    "120": 6,
    "121": 6,
    "122": 6,
    "123": 6,
    "130": 7,
    "131": 7,
    "132": 7,
    "133": 7,
    "200": 8,
    "201": 8,
    "202": 8,
    "203": 8,
    "210": 9,
    "211": 9,
    "212": 9,
    "213": 9,
    "220": 10,
    "221": 10,
    "222": 10,
    "223": 10,
    "230": 11,
    "231": 11,
    "232": 11,
    "233": 12,
    "300": 12,
    "301": 12,
    "302": 13,
    "303": 13,
    "310": 13,
    "311": 14,
    "312": 14,
    "313": 14,
    "320": 15,
    "321": 15,
    "322": 15,
    "323": "S",
    "330": "F",
    "331": "F",
    "332": "F",
    "333": "F",
}

def decrypt_splited_codons(splited_codons):
    decrypted_data = ""
    for codon in splited_codons:
        decoded_block = codon_table_to_decode[codon]
        if decoded_block == "S":
            continue
        elif decoded_block == "F":
            print(decrypted_data)
            return decrypted_data
        else:
            decrypted_data = decrypted_data + hex(decoded_block).replace("0x", "")

encrypted_codons = input("encrypted_codons: ")
decrypted_data = ""
splited_codons = [encrypted_codons[i:i+3] for i in range(0, len(encrypted_codons), 3)]
decrypted_text = decrypt_splited_codons(splited_codons)
chars = bytes([int(decrypted_text[i:i+2], 16) for i in range(0, len(decrypted_text), 2)])
print(chars.decode("utf-8"))