import argparse
import pathlib
import re
from dataclasses import dataclass, field

from markdown_it import MarkdownIt
from markdown_it.token import Token
from mdit_py_plugins.front_matter import front_matter_plugin

RE_API_TYPE = re.compile(r'-api-type: winrt ([a-z]+)')


@dataclass
class WinRTPage:
    title: str = ''
    description: list[Token] = field(default_factory=list)
    remarks: list[Token] = field(default_factory=list)
    examples: list[Token] = field(default_factory=list)
    see_also: list[Token] = field(default_factory=list)


@dataclass
class WinRTEnumField:
    name: str
    value: int
    description: list[Token]


@dataclass
class WinRTEnum(WinRTPage):
    fields: list[WinRTEnumField] = field(default_factory=list)


@dataclass
class WinRTProperty(WinRTPage):
    property_value: str = ''


@dataclass
class WinRTMethodParameter:
    name: str
    description: list[Token]


@dataclass
class WinRTMethod(WinRTPage):
    parameters: list[WinRTMethodParameter] = field(default_factory=list)


@dataclass
class WinRTClass(WinRTPage):
    properties: list[WinRTProperty] = field(default_factory=list)
    methods: list[WinRTMethod] = field(default_factory=list)


@dataclass
class WinRTNamespace(WinRTPage):
    classes: dict[str, WinRTClass] = field(default_factory=dict)
    enums: list[WinRTEnum] = field(default_factory=list)


def parse_projections(root_folder: pathlib.Path):
    md = MarkdownIt().use(front_matter_plugin)
    for folder in root_folder.iterdir():
        if folder.is_dir():
            pages = list(folder.glob('*.md'))
            if len(pages) == 0:
                print(f'skipping {folder} - not a namespace folder')
                continue
            # TODO ensure files are ordered so that classes always come before their methods and properties
            ns = WinRTNamespace()
            for page in pages:
                with page.open(encoding='utf-8') as f:
                    tokens = md.parse(f.read())
                props = {}

                token = tokens.pop(0)
                assert token.type == 'front_matter', token
                doc_type = RE_API_TYPE.search(token.content).group(1)

                token = tokens.pop(0)
                # there can be an HTML comment with the element signature before the title
                if token.type == 'html_block':
                    token = tokens.pop(0)
                assert token.type == 'heading_open' and token.tag == 'h1'
                token = tokens.pop(0)
                assert token.type == 'inline'
                props['name'] = token.content
                token = tokens.pop(0)
                assert token.type == 'heading_close' and token.tag == 'h1'

                while len(tokens) > 0:
                    token = tokens.pop(0)
                    assert token.type == 'heading_open' and token.tag == 'h2'
                    token = tokens.pop(0)
                    assert token.type == 'inline'
                    prop = token.content
                    token = tokens.pop(0)
                    assert token.type == 'heading_close' and token.tag == 'h2'

                    # TODO special handling for -enum-fields and -parameters
                    # TODO set props[prop] as everything preceding the next h2

                # TODO create element (or set ns properties) according to doc_type

            # TODO convert names to Python conventions
            # TODO convert relative links to xrefs
            # TODO generate namespace files


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="generate documentation on projections from Microsoft's DocFX source")
    parser.add_argument('source', type=pathlib.Path, help='path to WinRT documentation')
    # TODO argument for things to skip
    args = parser.parse_args()
    parse_projections(args.source)
