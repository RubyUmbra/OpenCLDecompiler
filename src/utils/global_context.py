_CONTEXT = None


class _Context:
    def __init__(self):
        self._data = {}

    def update(self, **kwargs):
        self._data.update(**kwargs)

    def remove(self, key: str):
        del self._data[key]

    def contains(self, key: str) -> bool:
        return key in self._data

    def get(self, key: str) -> any:
        return self._data[key]


def get_context() -> _Context:
    global _CONTEXT
    if not _CONTEXT:
        _CONTEXT = _Context()

    return _CONTEXT
