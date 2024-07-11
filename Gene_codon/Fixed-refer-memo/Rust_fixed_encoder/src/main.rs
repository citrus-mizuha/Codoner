use rand::seq::SliceRandom;
use rand::thread_rng;
use std::collections::HashMap;
use std::io::{self, Write};

fn string_to_binary(input_string: &str) -> String {
    input_string
        .as_bytes()
        .iter()
        .map(|byte| format!("{:08b}", byte))
        .collect()
}

fn split_into_chunks(binary_string: &str) -> Vec<String> {
    binary_string
        .as_bytes()
        .chunks(4)
        .map(|chunk| String::from_utf8_lossy(chunk).to_string())
        .collect()
}

fn encrypt_data(chunks: Vec<String>, codon_table: &HashMap<u8, Vec<&str>>) -> Vec<String> {
    let mut encrypted_data: Vec<String> = Vec::new();
    for chunk in chunks {
        if let Ok(value) = u8::from_str_radix(&chunk, 2) {
            if let Some(codon_choices) = codon_table.get(&value) {
                let chosen_codon = codon_choices.choose(&mut thread_rng()).unwrap_or(&"Invalid").to_string();
                encrypted_data.push(chosen_codon);
            } else {
                encrypted_data.push("Invalid".to_string());
            }
        } else {
            encrypted_data.push("Invalid".to_string());
        }
    }

    encrypted_data.insert(0, "323".to_string());
    let choices = ["330", "331", "332", "333"];
    encrypted_data.push(choices.choose(&mut thread_rng()).unwrap().to_string());

    encrypted_data
}

fn convert_to_binary(encrypted_data: Vec<String>) -> String {
    encrypted_data.join("")
}

fn main() {
    let codon_table: HashMap<u8, Vec<&str>> = [
        (0, vec!["000", "001", "002", "003"]),
        (1, vec!["010", "011", "012", "013"]),
        (2, vec!["020", "021", "022", "023"]),
        (3, vec!["030", "031", "032", "033"]),
        (4, vec!["100", "101", "102", "103"]),
        (5, vec!["110", "111", "112", "113"]),
        (6, vec!["120", "121", "122", "123"]),
        (7, vec!["130", "131", "132", "133"]),
        (8, vec!["200", "201", "202", "203"]),
        (9, vec!["210", "211", "212", "213"]),
        (10, vec!["220", "221", "222", "223"]),
        (11, vec!["230", "231", "232"]),
        (12, vec!["233", "300", "301"]),
        (13, vec!["302", "303", "310"]),
        (14, vec!["311", "312", "313"]),
        (15, vec!["320", "321", "322"]),
    ].iter().cloned().collect();

    let mut input_string = String::new();
    print!("文字列 : ");
    io::stdout().flush().unwrap();
    io::stdin().read_line(&mut input_string).unwrap();
    let input_string = input_string.trim();

    let utf8_binary = string_to_binary(&input_string);
    println!("UTF-8 Binary: {}", utf8_binary);

    let binary_chunks = split_into_chunks(&utf8_binary);
    println!("Binary Chunks: {:?}", binary_chunks);

    let encrypted_data = encrypt_data(binary_chunks, &codon_table);
    println!("Pseudo-Quaternary: {:?}", encrypted_data);

    let converted_binary = convert_to_binary(encrypted_data);
    println!("Converted Binary: {}", converted_binary);
}
