import argparse
import pathlib
import re
from dataclasses import dataclass, field

from markdown_it import MarkdownIt
from markdown_it.token import Token
from mdit_py_plugins.front_matter import front_matter_plugin

RE_API_TYPE = re.compile(r'-api-type: winrt ([a-z]+)')
RE_ENUM_FIELD = re.compile(r'-field (?P<name>[A-Za-z]+):(?P<value>\d+)')
RE_STRUCT_FIELD = re.compile(r'-field ([A-Za-z]+)')
RE_METHOD_PARAM = re.compile(r'-param ([A-Za-z]+)')


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
class WinRTStructField:
    name: str
    description: list[Token]


@dataclass
class WinRTStruct(WinRTPage):
    fields: list[WinRTStructField] = field(default_factory=list)


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
                with page.open(encoding='utf-8', errors='ignore') as f:
                    tokens = md.parse(f.read())
                props = {}

                token = tokens.pop(0)
                assert token.type == 'front_matter', f.name
                doc_type = RE_API_TYPE.search(token.content).group(1)

                token = tokens.pop(0)
                # there can be an HTML comment with the element signature before the title
                if token.type == 'html_block':
                    token = tokens.pop(0)
                if token.type != 'heading_open' or token.tag != 'h1':
                    print(f'missing title header on file {f.name} - skipped')
                    continue
                token = tokens.pop(0)
                assert token.type == 'inline', f.name
                props['name'] = token.content
                token = tokens.pop(0)
                assert token.type == 'heading_close' and token.tag == 'h1', f.name

                while len(tokens) > 0:
                    token = tokens.pop(0)
                    if token.type == 'html_block':  # ...also after the title
                        token = tokens.pop(0)
                    if token.type != 'heading_open' or token.tag != 'h2':
                        print(f'unexpected structure on file {f.name} - skipped')
                        break
                    token = tokens.pop(0)
                    assert token.type == 'inline', f.name
                    prop = token.content
                    token = tokens.pop(0)
                    assert token.type == 'heading_close' and token.tag == 'h2', f.name

                    if prop == '-enum-fields':
                        props['fields'] = []
                        while tokens[0].tag == 'heading_open' and tokens[0].tag == 'h3':
                            tokens.pop(0)
                            token = tokens.pop(0)
                            assert token.type == 'inline', f.name
                            field = RE_ENUM_FIELD.search(token.content).groupdict()
                            token = tokens.pop(0)
                            assert token.type == 'heading_close' and token.tag == 'h3', f.name
                            props['fields'].append(WinRTEnumField(description=tokens[:3], **field))
                            tokens = tokens[3:]
                    elif prop == '-struct-fields':
                        props['fields'] = []
                        while tokens[0].tag == 'heading_open' and tokens[0].tag == 'h3':
                            tokens.pop(0)
                            token = tokens.pop(0)
                            assert token.type == 'inline', f.name
                            field_name = RE_STRUCT_FIELD.search(token.content).group(0)
                            token = tokens.pop(0)
                            assert token.type == 'heading_close' and token.tag == 'h3', f.name
                            props['fields'].append(WinRTStructField(name=field_name, description=tokens[:3]))
                            tokens = tokens[3:]
                    elif prop == '-parameters':
                        props['fields'] = []
                        while tokens[0].tag == 'heading_open' and tokens[0].tag == 'h3':
                            tokens.pop(0)
                            token = tokens.pop(0)
                            assert token.type == 'inline', f.name
                            field_name = RE_METHOD_PARAM.search(token.content).group(0)
                            token = tokens.pop(0)
                            assert token.type == 'heading_close' and token.tag == 'h3', f.name
                            props['fields'].append(WinRTMethodParameter(name=field_name, description=tokens[:3]))
                            tokens = tokens[3:]
                    else:
                        props[prop[1:]] = []
                        while len(tokens) > 0 and (tokens[0].tag != 'heading_open' or tokens[0].tag != 'h2'):
                            props[prop[1:]].append(tokens.pop())

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
