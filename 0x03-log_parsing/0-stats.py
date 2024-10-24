#!/usr/bin/python3
import sys
import re

# Initialize counters and variables
total_file_size = 0
status_code_counts = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0,
}
line_count = 0

# Regex pattern to match the log format
log_pattern = re.compile(
    r'\s*(?P<ip_address>\S+) - \[(?P<timestamp>[^\]]+)\] "GET /projects/260 HTTP/1.1" (?P<status_code>\d{3}) (?P<file_size>\d+)'
)

def print_statistics():
    '''Prints the accumulated statistics.'''
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_code_counts.keys()):
        if status_code_counts[status_code] > 0:
            print(f"{status_code}: {status_code_counts[status_code]}")

try:
    for line in sys.stdin:
        match = log_pattern.match(line)
        if match:
            # Extract status code and file size
            status_code = match.group('status_code')
            file_size = int(match.group('file_size'))
            
            # Update total file size and status code count if valid
            total_file_size += file_size
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
            
            line_count += 1

            # Print statistics after every 10 lines
            if line_count % 10 == 0:
                print_statistics()

except KeyboardInterrupt:
    # Handle interruption and print final statistics
    print_statistics()
    sys.exit(0)

# Final statistics after EOF
print_statistics()

