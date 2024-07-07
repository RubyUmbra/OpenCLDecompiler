import functools

from parsers.base.base_parser import BaseParser
from parsers.parse_objects.base import ParseObject


class OneOrMoreParser(BaseParser):
    def __init__(self, parser: BaseParser):
        self._parser = parser

    def parse(self, text: str) -> tuple[ParseObject, str] | None:
        parse_result = self._parser.parse(text)

        if parse_result is None:
            return None

        results = []

        while True:
            result, rest = parse_result
            results.append(result)

            parse_result = self._parser.parse(rest)

            if parse_result is None:
                break

        return functools.reduce(lambda x, y: x + y, results), rest
