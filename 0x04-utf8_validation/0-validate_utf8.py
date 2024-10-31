#!/usr/bin/python3
'''Solution for validating UTF-8 encoded data'''

def validUTF8(data):
    # Helper function to check if a byte is a continuation byte (begins with '10')
    def is_continuation_byte(byte):
        return byte & 0b11000000 == 0b10000000

    total_bytes = len(data)
    i = 0

    while i < total_bytes:
        first_byte = data[i]

        # Check if it's a 1-byte character (begins with '0')
        if first_byte & 0b10000000 == 0:
            i += 1
            continue

        # Determine byte count in character based on leading bits
        num_bytes = 0
        if first_byte & 0b11100000 == 0b11000000:
            num_bytes = 2
        elif first_byte & 0b11110000 == 0b11100000:
            num_bytes = 3
        elif first_byte & 0b11111000 == 0b11110000:
            num_bytes = 4
        else:
            return False  # Invalid leading byte pattern for multi-byte character

        # Check if there are enough bytes left for this character
        if i + num_bytes > total_bytes:
            return False

        # Verify continuation bytes (each should start with '10')
        for j in range(1, num_bytes):
            if not is_continuation_byte(data[i + j]):
                return False

        # Move to the next character in the data array
        i += num_bytes

    return True

