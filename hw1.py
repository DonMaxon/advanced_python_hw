from sys import stdin

import click


@click.group()
def main():
    pass


@main.command(
    "nl",
)
@click.argument("input_file", type=click.File('r', encoding='utf-8'), default=stdin, required=False)
def number_lines(input_file):
    line_number = 1
    line: str
    if input_file!=stdin:
        for line in input_file.readlines():
            print(f"{line_number}\t{line}")
            line_number += 1
        if 'line' in locals() and line.endswith('\n'): #if the last string is empty
            print(f"{line_number}\t{''}")
    else:
        for line in input_file:
            print(f"{line_number}\t{line.strip()}")
            line_number += 1

def tail_for_file(file):
    try:
        lines_list = file.readlines()
        start = max(0, len(lines_list) - 10)
        for line in lines_list[start:]:
            print(line, end='')
    except FileNotFoundError:
        print(f"tail: {file.name}: No such file or directory")

@main.command(
    "tail",
)
@click.argument("input_files", type=click.File('r', encoding='utf-8'), nargs=-1)
def tail(input_files):
    if len(input_files)>0:
        print(len(input_files))
        for file in input_files:
            print(f"==> {file.name} <==")
            tail_for_file(file)
            print()
    else:
        for line in stdin.readlines()[-17:]:
            print(line, end='')

def wc(file):
    lines = 0
    words = 0
    chars = 0

    try:
        line: str
        for line in file.readlines():
            lines += 1
            words += len(line.split())
            chars += len(line)
        print(f"{lines}\t{words}\t{chars}\t{file.name}")
        return lines, words, chars
    except FileNotFoundError:
        print(f"wc: {file.name}: No such file or directory")

@main.command(
    "wc",
)
@click.argument("input_files", type=click.File('r', encoding='utf-8'), nargs=-1, required=False)
def word_count(input_files):
    total_lines = 0
    total_words = 0
    total_chars = 0

    if len(input_files)>0:
        for file in input_files:
            lines, words, chars = wc(file)
            total_lines += lines
            total_words += words
            total_chars += chars
        if len(input_files) > 1:
            print(f"{total_lines}\t{total_words}\t{total_chars}\ttotal")
    else:
        lines = 0
        words = 0
        chars = 0
        for line in stdin.readlines():
            lines += 1
            words += len(line.split())
            chars += len(line)
        print(f"{lines}\t{words}\t{chars}")


if __name__ == "__main__":
    main()