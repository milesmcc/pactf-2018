# Getting to know GDB

The competitor is provided with a binary that spits out the following output:

```
This is the string you're allowed to see...
  It is here for viewing, no matter what your intention may be...

But something more interesting below this sea...
  Fortunately for you, there is such a thing as GDB!

The solution is simple, but you have been baited...
  For the println that reveals the flag has been truncated!

The flag was in there, all ready to go–but not anymore...
  Now all that remains is some random base 64!

The flag is:
 --> Nm9VVjdPMnliQVNlZnJmaw== <--
```

This binary is compiled from Rust, which adds an additional layer of complexity to the problem. The `The flag is: ` line is actually a split string; the full string in memory is computed as follows:

```rust
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
```

...and printed like so:

```rust
unsafe {
    println!("{}", flag.slice_unchecked(0, 12));
}
```

Because the flag is encoded in binary, it is not possible to use the `strings` command to trivially find the flag. However, because the flag is dynamically converted to an ASCII string in memory at runtime, it is still _possible_ to pull the string from the binary. As such, it is also possible to pull the string from memory using a binary analysis program.

Doing so yields the following flag: `why_use_breakpoints_if_you_have_good_timing`
