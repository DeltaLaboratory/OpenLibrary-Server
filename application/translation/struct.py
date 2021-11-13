import pydantic as _pydantic


class Translation(_pydantic.BaseModel):
    config: str
    upload: str
    save: str
    library: str
    author: str
    writer: str
    illustrator: str
    translator: str
    publisher: str
    series: str
    version: str
    user: str
    user_name: str
    user_email: str
    download: str
    downloads: str
    ratings: str
