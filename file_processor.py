import re
import sys
import evaluator


token_list = [
    (r'[ \t]+',                 None),  # Spaces and Tabs
    (r'/\*[\s\S]*?\*/|//.*',    None),  # Comments
    (r'\r\n?|\n',               None),  # New line

    # Integer and String
    (r'\"[^\"\n]*\"',           "string"),
    (r'\'[^\'\n]*\'',           "string"),
    (r'[\+\-]?[0-9]*\.[0-9]+',  "float"),
    (r'[\+\-]?[1-9][0-9]+',     "integer"),
    (r'[\+\-]?[0-9]',           "integer"),

    # Operators
    (r'\+',                     "+"),
    (r'\-',                     "-"),
    (r'\*',                     "*"),
    (r'\/',                     "/"),
    (r'\%',                     "%"),
    (r'\-',                     "-"),
    (r'\-',                     "-"),
    (r'\=',                     "="),

    # Keyword
    (r'\bbreak\b',              "break"),
    (r'\bconst\b',              "const"),
    (r'\bcase\b',               "case"),
    (r'\bcatch\b',              "catch"),
    (r'\bcontinue\b',           "continue"),
    (r'\bdefault\b',            "default"),
    (r'\bdelete\b',             "delete"),
    (r'\belse\b',               "else"),
    (r'\bfalse\b',              "false"),
    (r'\bfinally\b',            "finally"),
    (r'\bfor\b',                "for"),
    (r'\bfunction\b',           "function"),
    (r'\bif\b',                 "if"),
    (r'\blet\b',                "let"),
    (r'\bnull\b',               "null"),
    (r'\breturn\b',             "return"),
    (r'\bswitch\b',             "switch"),
    (r'\bthrow\b',              "throw"),
    (r'\btry\b',                "try"),
    (r'\btrue\b',               "true"),
    (r'\bvar\b',                "var"),
    (r'\bwhile\b',              "while"),
    (r'\bnew\b',                "new"),

    # Misc
    (r'\(',                     "("),
    (r'\)',                     ")"),
    (r'\[',                     "["),
    (r'\]',                     "]"),
    (r'\{',                     "{"),
    (r'\}',                     "}"),
    (r'\<',                     "<"),
    (r'\>',                     ">"),
    (r'\.',                     "."),
    (r'\,',                     ","),
    (r'\:',                     ":"),
    (r'\;',                     ";"),
    (r'\'',                     "'"),
    (r'\"',                     "\""),
    (r'\|',                     "|"),
    (r'\&',                     "&"),
    (r'\!',                     "!"),

    (r'[A-Za-z_]\w*',           "variable"),
]


def tokenizer(file_content, token_list):
    """
    Returns a list of tokens
    :param str file_content: string containing the whole unmodified file content
    :param list[tuple[str, None] | tuple[str, str]] token_list:
    :return: list containing tokens
    :rtype: list[str]
    """

    pos = 0  # character position in the whole file_content
    cur = 1  # matched string position in its current line
    line = 1  # current line
    tokens = []

    while pos < len(file_content):

        if file_content[pos] == '\n':
            cur = 1
            line += 1

        match = None

        for t in token_list:
            pattern, tag = t

            regex = re.compile(pattern)
            match = regex.match(file_content, pos)

            if match:

                if tag:

                    if tag == "variable":
                        operation_string = match.string[match.start():match.end()]

                        if evaluator.check_variable.accepts_input(operation_string):
                            token = tag
                            tokens.append(token)
                        else:
                            break
                    else:
                        token = tag
                        tokens.append(token)

                break

        if not match:
            print("Syntax Error!")
            print(f'Terjadi kesalahan pada line {line}!')
            sys.exit(1)
        else:
            pos = match.end(0)
        cur += 1

    return tokens


def create_token_string(file_path):
    """
    Converts file content into a string containing tokens joined by a space (" ").
    :param str file_path: Input file path
    :return: string in which the file content is already converted into tokens and joined by a space (" ").
    :rtype: str
    """

    file = open(file_path)
    file_content = file.read()
    file.close()

    tokens = tokenizer(file_content, token_list)
    token_array = []

    for token in tokens:
        token_array.append(token)

    return " ".join(token_array)


if __name__ == "__main__":
    token_string = create_token_string("js.txt")
    print(token_string)
