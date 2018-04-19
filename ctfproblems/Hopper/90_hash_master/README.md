# Hash Master
The competitor is presented with a hash (`293366475`) that they must 'reverse'. They are given the following hashing algorithm:

```python
def hash_it(string):
    q = 0
    z = 127
    for i in [int(byte) for byte in bytearray(string, "utf-8")]:
        q += i
        z *= i
    return (((q << 3)+1)*z) % (2**32 - 1)
```

The flag is anything that hashes to `293366475`, and `aaaaab` will do the trick.
