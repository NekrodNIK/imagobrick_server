from PIL import Image
from fastapi import FastAPI

from modules.image_manipulate import gen_bricked_image
from modules.models import RequestModel, ResponseModel, ImageModel

app = FastAPI()


@app.post("/gen/image", response_model=ResponseModel)
def gen_image(request: RequestModel):
    generated_image = gen_bricked_image(
        Image.frombytes(data=request.image.data,
                        size=(request.image.width,
                              request.image.height),
                        mode="RGB"),
    )

    response = ResponseModel()
    response.image = ImageModel(data=generated_image.tobytes(),
                                width=generated_image.width,
                                height=generated_image.height)
    return response

