from PIL import Image
from fastapi import FastAPI

from modules.image_manipulate import gen_bricked_image
from modules.models import GenRequestModel

app = FastAPI()


@app.post("/gen/image")
def gen_image(request: GenRequestModel):
    return gen_bricked_image(image=Image.frombytes(data=bytes,
                                                   mode="RGB",
                                                   size=(request.image.width,
                                                         request.image.height)),
                             pixel_resolution=request.pixel_resolution,
                             color_count=request.pixel_resolution,
                             method_quantize=request.method_quantize)
