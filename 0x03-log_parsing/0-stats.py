#!/usr/bin/python3
'''Log parsing solution that reads logs, tracks file size and status codes, and prints statistics'''
import sys
import re


def initialize_log_metrics():
    '''Initializes log metrics with a file size counter and a dictionary to count status codes'''
    status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    log_metrics = {"total_file_size": 0,
                   "status_code_counts": {str(code): 0 for code in status_codes}}
    return log_metrics


def parse_log_line(line, pattern, log_metrics):
    '''Parses a single line from log input, updating file size and status code counts if the format is valid'''
    match = pattern.fullmatch(line)

    if match:
        status_code, file_size = match.group(1, 2)

        # Update total file size
        log_metrics["total_file_size"] += int(file_size)

        # Update count for the specific status code if it's valid
        if status_code.isdecimal():
            log_metrics["status_code_counts"][status_code] += 1
    return log_metrics


def display_log_metrics(log_metrics):
    '''Prints total file size and counts for each status code that has been encountered'''
    print("File size: {}".format(log_metrics['total_file_size']))
    for code in sorted(log_metrics["status_code_counts"]):
        if log_metrics["status_code_counts"][code]:
            print(f"{code}: {log_metrics['status_code_counts'][code]}")


def main():
    '''Main function that reads log lines from stdin and periodically displays metrics'''
    # Regex pattern to match the expected log format
    log_pattern = re.compile(
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)'
    )
    log_metrics = initialize_log_metrics()
    line_count = 0

    # Process each line from standard input
    for line in sys.stdin:
        line = line.strip()
        line_count += 1
        parse_log_line(line, log_pattern, log_metrics)

        # Every 10 lines, print the current metrics
        if line_count % 10 == 0:
            display_log_metrics(log_metrics)

    # Print final metrics if there are fewer than 10 lines remaining
    display_log_metrics(log_metrics)


if __name__ == '__main__':
    main()

