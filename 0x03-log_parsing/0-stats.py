#!/usr/bin/python3
'''A script for parsing and analyzing HTTP request logs.
'''
import re


def extract_log_data(log_line):
    '''Extracts various components from a line in an HTTP request log.
    '''
    log_pattern = (
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
        log_pattern[0], log_pattern[1], log_pattern[2], log_pattern[3], log_pattern[4]
    )
    match = re.fullmatch(log_format, log_line)
    if match is not None:
        status_code = match.group('status_code')
        file_size = int(match.group('file_size'))
        log_info['status_code'] = status_code
        log_info['file_size'] = file_size
    return log_info


def display_metrics(total_size, status_code_count):
    '''Displays the aggregated log metrics such as file size and status codes.
    '''
    print('File size: {:d}'.format(total_size), flush=True)
    for status_code in sorted(status_code_count.keys()):
        count = status_code_count.get(status_code, 0)
        if count > 0:
            print('{:s}: {:d}'.format(status_code, count), flush=True)


def update_statistics(log_line, total_size, status_code_count):
    '''Updates the total file size and status code counts based on a log line.

    Args:
        log_line (str): A line of HTTP request log data.

    Returns:
        int: The updated total file size.
    '''
    log_data = extract_log_data(log_line)
    status_code = log_data.get('status_code', '0')
    if status_code in status_code_count.keys():
        status_code_count[status_code] += 1
    return total_size + log_data['file_size']


def run_parser():
    '''Executes the log parsing process.
    '''
    log_count = 0
    total_file_size = 0
    status_code_count = {
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
                status_code_count,
            )
            log_count += 1
            if log_count % 10 == 0:
                display_metrics(total_file_size, status_code_count)
    except (KeyboardInterrupt, EOFError):
        display_metrics(total_file_size, status_code_count)


if __name__ == '__main__':
    run_parser()

