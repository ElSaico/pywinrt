import argparse
import pathlib
from dataclasses import dataclass, field
from typing import List, Dict

from markdown_it import MarkdownIt
from markdown_it.tree import SyntaxTreeNode
from mdit_py_plugins import front_matter


@dataclass
class WinRTPage:
    path: str = ''
    description: str = ''
    remarks: str = ''
    examples: str = ''
    see_also: str = ''  # could be a list of links?


@dataclass
class WinRTEnumField:
    name: str
    value: int
    description: str


@dataclass
class WinRTEnum(WinRTPage):
    fields: List[WinRTEnumField] = field(default_factory=list)


@dataclass
class WinRTProperty(WinRTPage):
    property_value: str = ''


@dataclass
class WinRTMethodParameter:
    name: str
    description: str


@dataclass
class WinRTMethod(WinRTPage):
    parameters: List[WinRTMethodParameter] = field(default_factory=list)


@dataclass
class WinRTClass(WinRTPage):
    properties: List[WinRTProperty] = field(default_factory=list)
    methods: List[WinRTMethod] = field(default_factory=list)


@dataclass
class WinRTNamespace(WinRTPage):
    classes: Dict[str, WinRTClass] = field(default_factory=dict)
    enums: List[WinRTEnum] = field(default_factory=list)


def parse_projections(root_folder: pathlib.Path):
    md = MarkdownIt().use(front_matter)
    for folder in root_folder.iterdir():
        if folder.is_dir():
            pages = list(folder.glob('*.md'))
            if len(pages) == 0:
                print(f'skipping {folder} - not a namespace folder')
                continue
            # TODO ensure files are ordered so that classes always come before their methods and properties
            ns = WinRTNamespace()
            for page in pages:
                with page.open() as f:
                    tokens = md.parse(f.read())
                tree = SyntaxTreeNode(tokens)
                # TODO check -api-type and handle accordingly


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="generate documentation on projections from Microsoft's DocFX source")
    parser.add_argument('source', type=pathlib.Path, help='path to WinRT documentation')
    # TODO argument for things to skip
    args = parser.parse_args()
    parse_projections(args.source)
