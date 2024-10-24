#!/usr/bin/python3
'''Script for parsing and analyzing HTTP request logs.
'''
import re


def extract_log_data(log_line):
    '''Extracts individual components from a line of an HTTP request log.
    '''
    log_patterns = (
        r'\s*(?P<ip_address>\S+)\s*',
        r'\s*\[(?P<timestamp>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request_line>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    log_info = {
        'status_code': 0,
        'file_size': 0,
    }
    log_format = '{}\\-{}{}{}{}\\s*'.format(
        log_patterns[0], log_patterns[1], log_patterns[2], log_patterns[3], log_patterns[4]
    )
    match = re.fullmatch(log_format, log_line)
    if match is not None:
        status_code = match.group('status_code')
        file_size = int(match.group('file_size'))
        log_info['status_code'] = status_code
        log_info['file_size'] = file_size
    return log_info


def display_statistics(total_file_size, status_code_counts):
    '''Displays the total file size and counts of each HTTP status code.
    '''
    print('File size: {:d}'.format(total_file_size), flush=True)
    for status_code in sorted(status_code_counts.keys()):
        count = status_code_counts.get(status_code, 0)
        if count > 0:
            print('{:s}: {:d}'.format(status_code, count), flush=True)


def update_statistics(log_line, total_file_size, status_code_counts):
    '''Updates the total file size and increments the count for the HTTP status code.

    Args:
        log_line (str): A line of HTTP request log data.

    Returns:
        int: The updated total file size.
    '''
    log_data = extract_log_data(log_line)
    status_code = log_data.get('status_code', '0')
    if status_code in status_code_counts.keys():
        status_code_counts[status_code] += 1
    return total_file_size + log_data['file_size']


def run_parser():
    '''Executes the log parsing and displays the statistics every 10 lines.
    '''
    line_count = 0
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
    try:
        while True:
            log_line = input()
            total_file_size = update_statistics(
                log_line,
                total_file_size,
                status_code_counts,
            )
            line_count += 1
            if line_count % 10 == 0:
                display_statistics(total_file_size, status_code_counts)
    except (KeyboardInterrupt, EOFError):
        display_statistics(total_file_size, status_code_counts)


if __name__ == '__main__':
    run_parser()

