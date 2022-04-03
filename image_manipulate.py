from enum import IntEnum

from PIL import Image, ImageEnhance


class MethodsQuantize(IntEnum):
    MEDIAN_CUT = 0
    MAX_COVERAGE = 1


def gen_bricked_image(image: Image,
                      pixel_resolution: int = 40,
                      color_count: int = 5,
                      method_quantize: MethodsQuantize.value = MethodsQuantize.MEDIAN_CUT) -> Image:
    image_man = image.resize((pixel_resolution, pixel_resolution), resample=Image.ADAPTIVE)

    image_man = \
        ImageEnhance.Contrast(image_man).enhance(pixel_resolution)

    image_man = image_man.quantize(colors=color_count)

    image_man = image_man.resize(image.size, resample=Image.NEAREST)

    return image_man
