"""Encodes given byte data in the last bit (or 2 bits) of each value in each channel of an RGB
image. The data is hidden in order r1, g1, b1, r2, g2, b2, etc., for each pixel in left-right
top-down order. The chosen byte data encodes a string that gives the flag, along with some filler to
pad the image size."""

from itertools import chain

# need PIL installed to work with images
from PIL import Image


def to_bit_array(byte):
    """Gets 8 bits from a byte."""
    arr = []
    curr = byte
    for i in range(8):
        arr.append(curr % 2)
        curr = curr // 2
    return list(reversed(arr))



def to_byte(bits):
    byte = 0
    for i, b in enumerate(reversed(bits)):
        byte += 2 ** i * b
    return byte


def split_bytes(bytedata, n_bits=1):
    """Splits bytes into groups of bits, with leftovers, as a list of lists."""
    bitarray = list(chain.from_iterable(map(to_bit_array, bytedata)))
    # chunk into given chunks, pad with 0
    while len(bytedata) % n_bits != 0:
        bitarray.append(0)
    chunks = []
    for i in range(0, len(bitarray)+1-n_bits, n_bits):
        chunks.append(bitarray[i:i+n_bits])
    return chunks


def replace_bits(byte, bits):
    bits_old = to_bit_array(byte)
    for i in range(len(bits)):
        bits_old[-i - 1] = bits[i]
    return to_byte(bits_old)

        
def encode_data(im_file, new_file, data, bits=1):
    """Saves a new image file encoded with the hidden data. Bits is the number of bits at the end of
    each channel value to modify. Data is just bytes to include. Raises ValueError if the image size
    does not allow encoding the data. Doesn't modify past what is necessary to hide the data."""
    im = Image.open(im_file)
    in_data = list(chain.from_iterable(im.getdata()))  # flatten
    new_data = []
    # error check
    if len(data) > bits * len(in_data):
        raise ValueError("Not enough space!")
    elif bits > 8:
        raise ValueError("Can't do more than 8 bits!")
    # get bit values to replace from data
    replacements = split_bytes(data)
    # in each 8 bits, replace it with the given data
    for i, byte in enumerate(in_data):
        if i < len(replacements):
            new_data.append(replace_bits(byte, replacements[i]))
        else:
            pass  # don't modify anything

    # now reconstitute data back into image
    # first chunk into 3-tuples
    pixels = []
    for i in range(0, len(new_data)-2, 3):
        pixels.append(tuple(new_data[i:i+3]))

    im.putdata(pixels)
    im.save(new_file)
    return (im, pixels)


MESSAGE = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut eleifend, metus accumsan accumsan
pharetra, dui justo lobortis augue, non bibendum sapien lacus a nulla. Praesent non libero et magna
ornare interdum. Vivamus et mi et justo tincidunt porttitor placerat in nisl. Nam mollis quam sit
amet iaculis volutpat. Nulla posuere pulvinar est, ac consectetur ex rhoncus non. Vivamus efficitur,
ex vel lobortis faucibus, massa neque iaculis libero, eu dictum orci odio ut ante. Phasellus luctus
magna vel euismod cursus. Donec et est rhoncus, lacinia metus in, sodales lectus. Sed posuere, nibh
vitae egestas rutrum, nisl odio iaculis urna, et bibendum dolor augue tristique lacus. Ut nunc
metus, blandit a nisl vitae, pulvinar fringilla justo. The flag is "last bits
matter". Congratulations! You cracked the code! """.replace('\n', '')
im, pixels = encode_data("last-bit-steganography/andover-blue.png",
                         "last-bit-steganography/true-blue.png",
                         MESSAGE.encode('ascii'))


def decode_data(pixels, n_bits):
    """Given pixel data, returns the message hidden."""
    byte = to_byte([0] * (8 - n_bits) + [1] * n_bits)
    bits = []
    for val in list(chain.from_iterable(pixels)):
        bits += list(reversed(to_bit_array(val & byte)))[:n_bits]
    # pad with 0's
    while len(bits) % 8 != 0:
        bits.append(0)
    message = []
    for i in range(0, len(bits) - 7, 8):
        message.append(to_byte(bits[i:i+8]))
    return bytes(message).decode('utf-8')
