#!/usr/bin/python3
'''UTF-8 validation solution'''

def validUTF8(data):
    def is_valid_byte(byte):
        # Check if the byte starts with '10', which means it's a continuation byte.
        return byte & 0b11000000 == 0b10000000

    n = len(data)
    i = 0

    while i < n:
        byte = data[i]

        # If the byte starts with '0', it's a 1-byte character.
        if byte & 0b10000000 == 0:
            i += 1
            continue

        # Determine the number of bytes based on the pattern at the start.
        num_bytes = 0
        if byte & 0b11100000 == 0b11000000:
            num_bytes = 2
        elif byte & 0b11110000 == 0b11100000:
            num_bytes = 3
        elif byte & 0b11111000 == 0b11110000:
            num_bytes = 4
        else:
            return False  # Invalid start byte pattern

        # Check if there are enough bytes left for this character.
        if i + num_bytes > n:
            return False

        # Validate that each following byte starts with '10'.
        for j in range(1, num_bytes):
            if not is_valid_byte(data[i + j]):
                return False

        # Move to the next character after validating the current multi-byte character.
        i += num_bytes

    return True

