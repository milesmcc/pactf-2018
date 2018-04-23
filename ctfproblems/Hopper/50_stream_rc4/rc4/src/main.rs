//! This file implements the RC4 cipher, which has some...vulnerabilities. The key length is 64 bits.

use std::io;

/// Initializes the keystream from a key.
fn initialize_stream(key: Vec<u8>) -> Vec<u8> {
    let mut s: Vec<u8> = vec![];
    let keylen = key.len();
    for i in 0..256 {
        s.push(i as u8);
    }
    let mut j: u8 = 0;
    for i in 0..256 {
        // get ith bit of key
        let key_bit: u8 = key[i % keylen];
        j = j.wrapping_add(s[i]).wrapping_add(key_bit);
        // swap S[i] and S[j]
        let swap = s[i as usize];
        s[i as usize] = s[j as usize];
        s[j as usize] = swap;
    }
    s
}

/// A state of the RC4 cipher.
#[derive(Debug, Hash, PartialEq, Eq, Clone)]
struct RC4 {
    s: Vec<u8>,
    i: u8,
    j: u8,
}

impl RC4 {
    fn from_key(key: Vec<u8>) -> RC4 {
        RC4 {
            s: initialize_stream(key),
            i: 0,
            j: 0
        }
    }

    /// Generates a single byte of output.
    fn gen_byte(&mut self) -> u8 {
        self.i = self.i.wrapping_add(1);
        self.j = self.j.wrapping_add(self.s[self.i as usize]);
        // swap S[i] and S[j]
        let i = self.i as usize;
        let j = self.j as usize;
        let swap = self.s[i];
        self.s[i] = self.s[j];
        self.s[j] = swap;
        self.s[(self.s[i].wrapping_add(self.s[j])) as usize]
            
    }

    fn gen_bytes(&mut self, n: usize) -> Vec<u8> {
        let mut bytes = vec![];
        for _ in 0..n {
            bytes.push(self.gen_byte());
        }
        bytes
    }
}

fn bytes_to_string(data: &[u8]) -> String {
    let mut s = String::new();
    for byte in data {
        s.push_str(&format!("{:02X}", byte));
    }
    s
}

fn main() {
    loop {
        println!("{}", "Please enter a key (ASCII text): ");
        let mut keystr = String::new();
        io::stdin().read_line(&mut keystr).unwrap();
        keystr.pop();
        let key = keystr.into_bytes();
        let mut rc4 = RC4::from_key(key);        
        println!("{}", "Message to encrypt: ");
        let mut message = String::new();
        io::stdin().read_line(&mut message).unwrap();
        message.pop();
        let message_bytes = message.into_bytes();
        let stream_bytes = rc4.gen_bytes(message_bytes.len());
        let mut cipher_bytes = vec![];
        for i in 0..(message_bytes.len()) {
            cipher_bytes.push(message_bytes[i] ^ stream_bytes[i]);
        }
        println!("{}\n{}", "Your coded message (in hexadecimal) is:", bytes_to_string(&cipher_bytes));
    }
}
