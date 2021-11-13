import json as _json

from ...structure.language import Language as _Language

REGISTERED_LANGUAGE = (
    _Language.Korean,
    _Language.English
)


def load_resource():
    resource = {}
    for language in REGISTERED_LANGUAGE:
        with open(f".{language}.json", "rt", encoding="utf-8") as file:
            resource[language] = _json.load(file)
