import typing as _typing

import pydantic as _pydantic


class Translator(_pydantic.BaseModel):
    global_id: _pydantic.UUID4
    name: str


class Illustrator(_pydantic.BaseModel):
    global_id: _pydantic.UUID4
    name: str


class Author(_pydantic.BaseModel):
    global_id: _pydantic.UUID4
    name: str


Writer = _typing.Union[
    _typing.List[
        Translator,
        Illustrator,
        Author,
    ],
    _typing.Tuple[
        Translator,
        Illustrator,
        Author
    ]
]
