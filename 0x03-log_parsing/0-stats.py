#!/usr/bin/python3
'''A script for parsing HTTP request logs and calculating statistics.
'''
import re


def extract_input(input_line):
    '''Extracts information from a line of an HTTP request log.

    Args:
        input_line (str): The log line to extract data from.

    Returns:
        dict: A dictionary containing the status code and file size from the log line.
    '''
    log_pattern = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    info = {
        'status_code': 0,
        'file_size': 0,
    }
    log_format = '{}\\-{}{}{}{}\\s*'.format(
        log_pattern[0], log_pattern[1], log_pattern[2], log_pattern[3], log_pattern[4]
    )
    match = re.fullmatch(log_format, input_line)
    if match:
        info['status_code'] = match.group('status_code')
        info['file_size'] = int(match.group('file_size'))
    return info


def print_statistics(total_file_size, status_codes_stats):
    '''Prints the total file size and the number of times each status code has been encountered.

    Args:
        total_file_size (int): The total size of all files.
        status_codes_stats (dict): Dictionary of status codes and their counts.
    '''
    print('File size: {:d}'.format(total_file_size), flush=True)
    for status_code in sorted(status_codes_stats.keys()):
        count = status_codes_stats.get(status_code, 0)
        if count > 0:
            print('{:s}: {:d}'.format(status_code, count), flush=True)


def update_metrics(line, total_file_size, status_codes_stats):
    '''Updates the metrics based on the current log line.

    Args:
        line (str): The line from the log to process.
        total_file_size (int): The current total file size.
        status_codes_stats (dict): The current status code counts.

    Returns:
        int: The updated total file size.
    '''
    line_info = extract_input(line)
    status_code = line_info.get('status_code', '0')
    if status_code in status_codes_stats:
        status_codes_stats[status_code] += 1
    return total_file_size + line_info['file_size']


def run():
    '''Starts the log parsing process and prints statistics every 10 lines or on interruption.
    '''
    line_num = 0
    total_file_size = 0
    status_codes_stats = {
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
            line = input()
            total_file_size = update_metrics(
                line, total_file_size, status_codes_stats
            )
            line_num += 1
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        print_statistics(total_file_size, status_codes_stats)


if __name__ == '__main__':
    run()

