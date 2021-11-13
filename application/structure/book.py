import pydantic as _pydantic

from .writer import Writer as _Writer
from .title import Title as _Title


class Book(_pydantic.BaseModel):
    global_id: _pydantic.UUID4
    title: _Title
    writer: _Writer
