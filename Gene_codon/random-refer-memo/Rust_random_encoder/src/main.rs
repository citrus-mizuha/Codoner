use rand::prelude::*;
use std::collections::HashMap;
use std::io::{self, Write};

fn generate_quaternary() -> String {
    let mut rng = rand::thread_rng();
    format!(
        "{}{}{}",
        rng.gen_range(0..=3),
        rng.gen_range(0..=3),
        rng.gen_range(0..=3)
    )
}

fn generate_codon_table() -> HashMap<String, Vec<String>> {
    let mut codon_table: HashMap<String, Vec<String>> = HashMap::new();
    for i in 0..=10 {
        let key = i.to_string();
        let values: Vec<String> = (0..4).map(|_| generate_quaternary()).collect();
        codon_table.insert(key, values);
    }
    for i in 11..=15 {
        let key = i.to_string();
        let values: Vec<String> = (0..3).map(|_| generate_quaternary()).collect();
        codon_table.insert(key, values);
    }
    codon_table.insert("S".to_string(), vec![generate_quaternary()]);
    codon_table.insert("F".to_string(), (0..4).map(|_| generate_quaternary()).collect());

    codon_table
}

fn string_to_binary(input: &str) -> String {
    input
        .bytes()
        .map(|b| format!("{:08b}", b))
        .collect::<Vec<String>>()
        .join("")
}

fn split_into_chunks(binary_string: &str) -> Vec<&str> {
    binary_string.as_bytes()
        .chunks(4)
        .map(std::str::from_utf8)
        .filter_map(Result::ok)
        .collect()
}

fn encrypt_data(chunks: Vec<&str>, codon_table: &HashMap<String, Vec<String>>) -> Vec<String> {
    let mut rng = rand::thread_rng();
    let mut encrypted_data: Vec<String> = Vec::new();

    for chunk in chunks {
        let value = usize::from_str_radix(chunk, 2).unwrap_or(usize::MAX);
        if let Some(codon_choices) = codon_table.get(&value.to_string()) {
            let chosen_codon = codon_choices[rng.gen_range(0..codon_choices.len())].clone();
            encrypted_data.push(chosen_codon);
        } else {
            encrypted_data.push("Invalid".to_string());
        }
    }

    encrypted_data.insert(0, "323".to_string());
    encrypted_data.push(
        ["330", "331", "332", "333"]
            .choose(&mut rng)
            .unwrap()
            .to_string(),
    );

    encrypted_data
}

fn convert_to_binary(encrypted_data: Vec<String>) -> String {
    encrypted_data.join("")
}

fn main() {
    let mut input_string = String::new();
    print!("文字列 : ");
    io::stdout().flush().unwrap();
    io::stdin().read_line(&mut input_string).unwrap();
    let input_string = input_string.trim();

    let codon_table = generate_codon_table();

    for (key, value) in &codon_table {
        println!("{}: {:?}", key, value);
    }

    let utf8_binary = string_to_binary(&input_string);
    println!("UTF-8 Binary: {}", utf8_binary);

    let binary_chunks = split_into_chunks(&utf8_binary);
    println!("Binary Chunks: {:?}", binary_chunks);

    let encrypted_data = encrypt_data(binary_chunks, &codon_table);
    println!("Pseudo-Quaternary: {:?}", encrypted_data);

    let converted_binary = convert_to_binary(encrypted_data);
    println!("Converted Binary: {}", converted_binary);
}
