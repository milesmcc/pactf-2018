extern crate base64;
extern crate rand;

use std::thread::sleep;
use std::time::Duration;
use rand::Rng;

fn main() {
    println!("This is the string you're allowed to see...");
    println!("  It is here for viewing, no matter what your intention may be...");
    println!();
    println!("But something more interesting below this sea...");
    println!("  Fortunately for you, there is such a thing as GDB!");
    println!();
    println!("The solution is simple, but you have been baited...");
    println!("  For the println that reveals the flag has been truncated!");
    println!();
    println!("The flag was in there, all ready to go–but not anymore...");
    println!("  Now all that remains is some random base 64!");
    println!();
    let flag: String = format!(
        "The flag is: {}",
        String::from_utf8(
            base64::decode(&base64::encode(&[
                0b01110111u8,
                0b01101000u8,
                0b01111001u8,
                0b01011111u8,
                0b01110101u8,
                0b01110011u8,
                0b01100101u8,
                0b01011111u8,
                0b01100010u8,
                0b01110010u8,
                0b01100101u8,
                0b01100001u8,
                0b01101011u8,
                0b01110000u8,
                0b01101111u8,
                0b01101001u8,
                0b01101110u8,
                0b01110100u8,
                0b01110011u8,
                0b01011111u8,
                0b01101001u8,
                0b01100110u8,
                0b01011111u8,
                0b01111001u8,
                0b01101111u8,
                0b01110101u8,
                0b01011111u8,
                0b01101000u8,
                0b01100001u8,
                0b01110110u8,
                0b01100101u8,
                0b01011111u8,
                0b01100111u8,
                0b01101111u8,
                0b01101111u8,
                0b01100100u8,
                0b01011111u8,
                0b01110100u8,
                0b01101001u8,
                0b01101101u8,
                0b01101001u8,
                0b01101110u8,
                0b01100111u8
            ] as &[u8])).unwrap()
        ).unwrap()
    );
    unsafe {
        println!("{}", flag.slice_unchecked(0, 12));
    }
    let mut generator = rand::thread_rng();
    loop {
        // let location = index % 50;
        // print!("\r{}*{}", std::iter::repeat("-").take(location).collect::<String>(), std::iter::repeat("-").take(49-location).collect::<String>());
        // index = index + 1;
        print!(
            "\r --> {} <--",
            base64::encode(&generator.gen_ascii_chars().take(16).collect::<String>())
        );
        sleep(Duration::from_millis(1));
    }
}
