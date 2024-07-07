from typing import Optional

from pyparsing import OneOrMore, Regex

from parsers.base.base_parser import BaseParser
from parsers.base.parser_element_parser import ParserElementParser
from parsers.parse_objects.base import ParseObject


class AnyParser(BaseParser):
    def parse(self, text: str) -> Optional[tuple[ParseObject, str]]:
        return ParserElementParser(OneOrMore(Regex("."))).parse(text)
