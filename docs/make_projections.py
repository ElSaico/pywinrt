import argparse
import pathlib
from markdown_it import MarkdownIt


def parse_projections(root_folder: pathlib.Path):
    ...


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="generate documentation on projections from Microsoft's DocFX source")
    parser.add_argument('source', type=pathlib.Path, help='path to WinRT documentation')
    args = parser.parse_args()
    parse_projections(args.source)
