"""
Enso standard library documentation generator.
"""
import argparse
from downloaders import download_stdlib, download_parser, download_stylesheet
from parse import init_parser, init_gen_dir, gen_all_files


def main(token: str) -> None:
    """
    Program entry point.
    """
    download_stdlib(token)
    download_parser()
    download_stylesheet()
    parser = init_parser()
    init_gen_dir()
    gen_all_files(parser)
    print("All done.")


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(
        description="Generates documentation sites for Enso Standard Library."
    )
    arg_parser.add_argument("token", help="GitHub user Personal Access Token.")
    args = arg_parser.parse_args()
    main(args.token)
