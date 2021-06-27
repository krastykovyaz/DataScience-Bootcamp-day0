import sys


def encode_char(char, bias):
    if not char.isalpha():
        return char
    new_char = ord(char) + bias
    if char.isupper() and new_char > ord('Z'):
        new_char -= 26
    if char.islower() and new_char > ord('z'):
        new_char -= 26
    return chr(new_char)


def decode_char(char, bias):
    if not char.isalpha():
        return char
    new_char = ord(char) - bias
    if char.isupper() and new_char < ord('A'):
        new_char += 26
    if char.islower() and new_char < ord('a'):
        new_char += 26
    return chr(new_char)


def transform_string(line: str, bias, mode):
    encoded_string = ''
    for char in line:
        encoded_string += (encode_char(char, bias)
                           if mode == 'encode' else decode_char(char, bias))
    return encoded_string


def check_argv():
    assert len(sys.argv) == 4, 'Invalid input'
    assert sys.argv[1] in ('decode', 'encode'), 'Invalid mode'
    assert sys.argv[2].isascii(), 'Invalid string'
    assert sys.argv[-1].isdigit() or 26 < int(sys.argv[-1]) < 0, 'Invalid bias'


def main():
    check_argv()
    transform_mode, string, caesar_bias = sys.argv[1:]
    caesar_bias = int(caesar_bias) % 26

    print(transform_string(string, caesar_bias, transform_mode))


if __name__ == '__main__':
    main()
