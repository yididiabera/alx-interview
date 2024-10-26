#!/usr/bin/python3
'''log parsing solution'''
import sys
import re
from signal import signal, SIGINT


def initialize_log():
    '''initializes log'''
    status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    log = {"file_size": 0,
           "code_list": {str(code): 0 for code in status_codes}}
    return log


def parse_line(line, regex, log):
    '''parses each line'''
    match = regex.fullmatch(line)

    if match:
        stat_code, file_size = match.group(1, 2)

        log["file_size"] += int(file_size)

        if stat_code.isdecimal() and stat_code in log["code_list"]:
            log["code_list"][stat_code] += 1
    return log


def print_codes(log):
    '''prints stats'''
    print("File size: {}".format(log['file_size']))
    sorted_code_list = sorted(log["code_list"])
    for code in sorted_code_list:
        if log["code_list"][code] > 0:
            print(f"{code}: {log['code_list'][code]}")


def main():
    '''Entry point'''
    regex = re.compile(
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)'
    )
    log = initialize_log()
    line_count = 0

    def handle_interrupt(signal_received, frame):
        '''Handle CTRL+C interruption'''
        print_codes(log)
        sys.exit(0)

    signal(SIGINT, handle_interrupt)

    for line in sys.stdin:
        line = line.strip()
        line_count += 1
        parse_line(line, regex, log)

        if line_count % 10 == 0:
            print_codes(log)

    print_codes(log)


if __name__ == '__main__':
    main()

