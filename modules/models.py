from typing import Literal, Optional

from pydantic import BaseModel


class ImageModel(BaseModel):
    data: bytes
    width: int
    height: int


class GenModel(BaseModel):
    image: ImageModel

    pixel_resolution: Optional[int]
    color_count: Optional[int]
    method_quantize: Optional[Literal["median_cut", "max_coverage"]]

    monochrome: Optional[bool]
    invert: Optional[bool]
    contrast: Optional[float]
