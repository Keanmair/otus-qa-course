import re
import os
import json
import argparse
from collections import Counter


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Process command line arguments.')
    parser.add_argument(
        '-p', '--path', help='Please indicate the path to the file', type=dir_path)
    parser.add_argument(
        '-f', '--file', help='Please indicate the file name', type=file_name)

    return parser.parse_args()


def dir_path(path):
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError(
            f"readable_dir:{path} is not a valid path")


def file_name(file):
    if os.path.isfile(file):
        return file
    else:
        raise argparse.ArgumentTypeError(
            f"readable_file:{file} is not a valid file")


def get_all_req(filename):
    regexp_req_type = r'GET|POST|PUT'

    with open(filename) as file:
        log = file.read()
        get_list = re.findall(regexp_req_type, log)
        return get_list


def get_ip_list(filename):
    regexp_ip = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

    with open(filename) as file:
        log = file.read()
        get_list = re.findall(regexp_ip, log)
        return get_list


def get_all_4xx_err(filename):
    regexp_req_type = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})+.*(POST|GET)+.*(400|401|403|404)" \
                      r"+.*(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)"

    with open(filename) as file:
        log = file.read()
        get_list = re.findall(regexp_req_type, log)
        return get_list


def get_all_5xx_err(filename):
    regexp_req_type = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})+.*(POST|GET)+.*(500|503|509|598)' \
                      r'+.*(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)'

    with open(filename) as file:
        log = file.read()
        get_list = re.findall(regexp_req_type, log)
        return get_list


def count_all_ip(get_list):
    count = Counter(get_list)
    return count


def count_top10_ip(get_list):
    count = Counter(get_list)
    return count.most_common(10)


def main():
    log = {}
    parsed_args = parse_arguments()
    res_top_ip = count_top10_ip(get_ip_list(parsed_args.file))
    res_get_post = count_all_ip(get_all_req(parsed_args.file))
    res_all_ent = len(get_ip_list(parsed_args.file))
    res_client_err = count_top10_ip(get_all_4xx_err(parsed_args.file))
    res_server_err = count_top10_ip(get_all_5xx_err(parsed_args.file))

    with open('output.json', 'w') as json_file:
        log['Parsed_log'] = {'Top 10 IPs list': res_top_ip,
                             'Top 10 client errors': res_client_err,
                             'Top 10 server errors': res_server_err,
                             'All GET and POST requests': res_get_post,
                             'All log entities': res_all_ent

                             }
        json.dump(log, json_file, indent=4)


if __name__ == "__main__":
    main()
