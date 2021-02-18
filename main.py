import sys
import getopt
import execjs
from download_helpers import *
from replace_all_occurences_in_file import *
from safe_create_dir import *

ORGANIZATION = "enso-org"
REPO = "enso"
BRANCH = "main"
DIRECTORY = "distribution/std-lib"
PARSER_COMMIT = "5e309bddcbec33cfbd150fcb8a16b45192cf5189"


def main(argv):
    download_stdlib(argv)
    download_parser()
    download_stylesheet()
    parser = init_parser()
    test_parse(parser)


def test_parse(parser):
    """
        Test if generating docs work.
        To be removed when created method to recursively generate all docfiles.
    """
    example = open('distribution/std-lib/Base/src/Math.enso', 'r').read()
    parsed = parser.call("$e_doc_parser_generate_html_source", example)
    out_dir = 'distribution/gen'
    safe_create_directory(out_dir)
    html_file = open(out_dir + '/Math.html', 'w')
    html_file.write('<link rel="stylesheet" href="../style.css"/>' + parsed)
    html_file.close()

    example = open('distribution/std-lib/Base/src/Meta.enso', 'r').read()
    parsed = parser.call("$e_doc_parser_generate_html_source", example)
    html_file = open(out_dir + '/Meta.html', 'w')
    html_file.write('<link rel="stylesheet" href="../style.css"/>' + parsed)
    html_file.close()


def init_parser():
    """
        Compiles JS parser to call from Python.
    """
    parser = open('distribution/parser.js', 'r').read()
    parser = execjs.compile(parser)
    return parser


def download_stylesheet():
    """
        Downloads stylesheet for docs from IDE repository.
    """
    repo_url = "https://raw.githubusercontent.com/enso-org/ide/"
    file_path = "develop/src/rust/ide/view/src/documentation/style.css"
    url = repo_url + file_path
    download_to = "distribution/temp-style.css"
    download_from_url(url, download_to)
    replace_all_occurrences_in_file(download_to,
                                    'distribution/style.css',
                                    '.docVis',
                                    'body')


def download_parser():
    """
        Downloads scala parser from Engine repository.
    """
    url = "https://packages.luna-lang.org/parser-js/nightly/"
    url = url + PARSER_COMMIT + "/scala-parser.js"
    download_to = "distribution/scala-parser.js"
    download_from_url(url, download_to)
    replace_all_occurrences_in_file(download_to,
                                    'distribution/parser.js',
                                    'export ',
                                    '// export')


def download_stdlib(argv):
    """
        Downloads Std-Lib from Engine repository.
    """
    token = ""
    try:
        opts, args = getopt.getopt(argv, "t:", ["token="])
    except getopt.GetoptError as err:
        print(str(err))
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-t", "--token"):
            token = arg
    download_from_git(token,
                      org=ORGANIZATION,
                      repo=REPO,
                      branch=BRANCH,
                      folder=DIRECTORY)


if __name__ == '__main__':
    main(sys.argv[1:])
