import pydantic as _pydantic


class Title(_pydantic.BaseModel):
    display_title: str
    search_title: str
