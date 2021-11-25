# generated by datamodel-codegen:
#   filename:  schema/type/profile.json
#   timestamp: 2021-11-20T15:09:34+00:00

from __future__ import annotations

from typing import Optional

from pydantic import AnyUrl, BaseModel


class ImageList(BaseModel):
    image: Optional[AnyUrl] = None
    image24: Optional[AnyUrl] = None
    image32: Optional[AnyUrl] = None
    image48: Optional[AnyUrl] = None
    image72: Optional[AnyUrl] = None
    image192: Optional[AnyUrl] = None
    image512: Optional[AnyUrl] = None


class Profile(BaseModel):
    images: Optional[ImageList] = None