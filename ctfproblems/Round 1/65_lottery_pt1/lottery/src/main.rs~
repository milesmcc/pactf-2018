#![feature(i128_type)]

extern crate rand;

use std::io;

use rand::{thread_rng, Rng};

const MULTIPLIER: u128 = 0x5DEECE66D;
const INCREMENT: u128 = 11;

fn read_input() -> i32 {
    let mut input = String::new();
    println!("{}", "What's your guess?");
    io::stdin().read_line(&mut input).unwrap();
    input.pop();
    let mut num_res = i32::from_str_radix(&input, 10);
    while num_res.is_err() {
        let mut input = String::new();
        println!("{}", "Not a valid number! Try again!");
        io::stdin().read_line(&mut input).unwrap();
        input.pop();
        num_res = i32::from_str_radix(&input, 10);
    }
    num_res.unwrap()
}

fn create_flag() -> String {
    // [77, 121, 32, 60, 51, 32, 105, 115, 32, 115, 112, 105, 108, 108, 101, 100] is the flag bytes
    let mut flag: Vec<u8> = vec![];
    flag.push(77);
    flag.push(121);
    flag.extend(vec![100, 101, 108, 108, 105, 112, 115, 32, 115, 105, 32, 51, 60,
                     32].iter().rev());
    String::from_utf8(flag).unwrap()
}

fn main() {
    println!("{}{}{}", "Feelin' lucky? Play the lottery! ",
             "Brought to you by Oracle Corporation free of charge! ",
             "Lottery numbers range from -2147483648 to 2147483647.");
    let mut rng = thread_rng();    
    let seed = rng.gen::<u64>() as u128;
    let seed = seed ^ MULTIPLIER & ((1u128 << 48) - 1);
    let mut state: u128 = seed;

    loop {
        // this is essentially an implementation of the Java RNG
        state = (state * MULTIPLIER + INCREMENT) & ((1u128 << 48) - 1);
        // remove everything up to 32 bits: was originally 48
        let truncated = state >> 16;
        let winning_num = truncated as i32;
        if read_input() == winning_num {
            println!("-------------");
            println!("{}{}\"{}\"", "You won the lottery! I can't give you a million dollars,",
                     " but I can give you the flag: ",
                     create_flag());
            println!("-------------");
            break;
        }
        else {
            println!("Better luck next time! Just to rub it in, {} was the winner!",
                     winning_num);
        }
    }
}
