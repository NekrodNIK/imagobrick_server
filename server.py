from PIL import Image
from fastapi import FastAPI

from modules.image_manipulate import gen_bricked_image
from modules.models import GenModel, ImageModel

app = FastAPI()


@app.post("/gen/image")
def gen_image(request: GenModel):
    generated_image = gen_bricked_image(
        Image.frombytes(data=request.image.data,
                        size=(request.image.width,
                              request.image.height),
                        mode="RGB"),
    )

    response = GenModel(image=ImageModel(
        data=generated_image.tobytes(),
        width=request.image.width,
        height=request.image.height
    ))
    return response

