import random


def generate_quaternary():
    return f"{random.randint(0, 3):01d}{random.randint(0, 3):01d}{random.randint(0, 3):01d}"


codon_table = {
    0: [generate_quaternary() for _ in range(4)],
    1: [generate_quaternary() for _ in range(4)],
    2: [generate_quaternary() for _ in range(4)],
    3: [generate_quaternary() for _ in range(4)],
    4: [generate_quaternary() for _ in range(4)],
    5: [generate_quaternary() for _ in range(4)],
    6: [generate_quaternary() for _ in range(4)],
    7: [generate_quaternary() for _ in range(4)],
    8: [generate_quaternary() for _ in range(4)],
    9: [generate_quaternary() for _ in range(4)],
    10: [generate_quaternary() for _ in range(4)],
    11: [generate_quaternary() for _ in range(3)],
    12: [generate_quaternary() for _ in range(3)],
    13: [generate_quaternary() for _ in range(3)],
    14: [generate_quaternary() for _ in range(3)],
    15: [generate_quaternary() for _ in range(3)],
    "S": [generate_quaternary()],
    "F": [generate_quaternary() for _ in range(4)]
}

input_string = input("文字列 : ")


def string_to_binary(input_string):
    utf8_bytes = input_string.encode('utf-8')
    binary_string = ''.join(format(byte, '08b') for byte in utf8_bytes)
    return binary_string


def split_into_chunks(binary_string):
    chunks = [binary_string[i:i + 4] for i in range(0, len(binary_string), 4)]
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

for key, value in codon_table.items():
    print(f"{key}: {value}")

print("UTF-8 Binary:", utf8_binary)
binary_chunks = split_into_chunks(utf8_binary)
print("Binary Chunks:", binary_chunks)
encrypted_data = encrypt_data(binary_chunks)
print("Pseudo-Quaternary:", encrypted_data)
converted_binary = convert_to_binary(encrypted_data)
print("Converted Binary:", converted_binary)

