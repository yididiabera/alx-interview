#!/usr/bin/python3
'''UTF-8 validation solution'''

def validUTF8(data):
    # Helper function to check if a byte is a continuation byte (starts with '10')
    def is_continuation_byte(byte):
        return byte & 0b11000000 == 0b10000000

    data_length = len(data)
    index = 0

    while index < data_length:
        current_byte = data[index]

        # Check for 1-byte character (starts with '0')
        if current_byte & 0b10000000 == 0:
            index += 1
            continue

        # Determine the number of bytes in the character based on leading bits
        char_length = 0
        if current_byte & 0b11100000 == 0b11000000:
            char_length = 2
        elif current_byte & 0b11110000 == 0b11100000:
            char_length = 3
        elif current_byte & 0b11111000 == 0b11110000:
            char_length = 4
        else:
            return False  # Invalid starting byte pattern for multi-byte character

        # Check if remaining bytes are sufficient for this character
        if index + char_length > data_length:
            return False

        # Validate continuation bytes (they should all start with '10')
        for offset in range(1, char_length):
            if not is_continuation_byte(data[index + offset]):
                return False

        # Move to the next character in the data list
        index += char_length

    return True

