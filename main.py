from argparse import ArgumentParser
from cyk import CYK
from cfg_converter import rulesparser, convert
from file_processor import create_token_string


if __name__ == "__main__":
    argument_parser = ArgumentParser()
    argument_parser.add_argument("path", type=str, help="Path file to parse")
    args = argument_parser.parse_args()

    cfg_result = rulesparser("cfg.txt")
    start_symbol = convert(cfg_result)[1]
    cnf_result = convert(cfg_result)[0]

    result = CYK(create_token_string(args.path), start_symbol, cnf_result)

    if result:
        print("String accepted")
    else:
        print("String rejected")
