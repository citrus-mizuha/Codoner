import random


def generate_unique_quaternaries():
    all_quaternaries = []
    for _ in range(64):
        while True:
            quaternary = f"{random.randint(0, 3):01d}{random.randint(0, 3):01d}{random.randint(0, 3):01d}"
            if quaternary not in all_quaternaries:
                all_quaternaries.append(quaternary)
                break
    return all_quaternaries


def create_random_trimap(unique_quaternaries):
    numbers = list(range(16))
    random.shuffle(numbers)
    four_count = set(numbers[:11])

    trimap = {}
    quaternary_index = 0

    for num in range(16):
        if num in four_count:
            trimap[num] = unique_quaternaries[quaternary_index:quaternary_index + 4]
            quaternary_index += 4
        else:
            trimap[num] = unique_quaternaries[quaternary_index:quaternary_index + 3]
            quaternary_index += 3

    trimap["S"] = [unique_quaternaries[quaternary_index]]
    quaternary_index += 1
    trimap["F"] = unique_quaternaries[quaternary_index:quaternary_index + 4]

    return trimap


unique_quaternaries = generate_unique_quaternaries()
trimap = create_random_trimap(unique_quaternaries)

# 以下、元のコードと同じ
input_string = input("文字列 : ")


def string_to_binary(input_string):
    utf8_bytes = input_string.encode('utf-8')
    binary_string = ''.join(format(byte, '08b') for byte in utf8_bytes)
    return binary_string


def split_into_chunks(binary_string):
    chunks = [binary_string[i:i + 4] for i in range(0, len(binary_string), 4)]
    return chunks


def encrypt_data(chunks):
    encoded_data = []
    for chunk in chunks:
        value = int(chunk, 2)
        if value in trimap:
            codon_choices = trimap[value]
            chosen_codon = random.choice(codon_choices)
            encoded_data.append(chosen_codon)
        else:
            encoded_data.append("Invalid")
    encoded_data.insert(0, "323")
    encoded_data.append(random.choice(["330", "331", "332", "333"]))
    return encoded_data


def convert_to_binary(encrypted_data):
    binary_string = ''.join(codon for codon in encrypted_data)
    return binary_string


utf8_binary = string_to_binary(input_string)

for key, value in trimap.items():
    print(f"{key}: {value}")

print("UTF-8 Binary:", utf8_binary)
binary_chunks = split_into_chunks(utf8_binary)
print("Binary Chunks:", binary_chunks)
encrypted_data = encrypt_data(binary_chunks)
print("Pseudo-Quaternary:", encrypted_data)
converted_binary = convert_to_binary(encrypted_data)
print("Converted Binary:", converted_binary)
