#!/usr/bin/python3
'''UTF-8 validation solution'''


def validUTF8(data):
    def is_valid_byte(byte):
        return byte & 0b11000000 == 0b10000000

    n = len(data)
    i = 0

    while i < n:
        byte = data[i]

        if byte & 0b10000000 == 0:
            i += 1
            continue

        num_bytes = 0
        if byte & 0b11100000 == 0b11000000:
            num_bytes = 2
        elif byte & 0b11110000 == 0b11100000:
            num_bytes = 3
        elif byte & 0b11111000 == 0b11110000:
            num_bytes = 4
        else:
            return False

        if i + num_bytes > n:
            return False

        for j in range(1, num_bytes):
            if not is_valid_byte(data[i + j]):
                return False

        i += num_bytes

    return True
