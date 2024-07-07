from parsers.base.base_parser import BaseParser
from parsers.parse_objects.base import ParseObject
from parsers.parse_objects.base.parse_object import EmptyParseObject


class OneOrZeroParser(BaseParser):
    def __init__(self, parser: BaseParser):
        self._parser = parser

    def parse(self, text: str) -> tuple[ParseObject, str] | None:
        parse_result = self._parser.parse(text)

        if parse_result is None:
            return EmptyParseObject(), text

        return parse_result
