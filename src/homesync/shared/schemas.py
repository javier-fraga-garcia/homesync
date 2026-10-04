from pydantic import BaseModel


class FileUpload(BaseModel):
    src_path: str
    content_hash: str


class FileMoved(BaseModel):
    src_path: str
    dest_path: str
