from enum import IntEnum

from PIL import ImageEnhance, ImageOps, Image


class MethodsQuantize(IntEnum):
    MEDIAN_CUT = 0
    MAX_COVERAGE = 1


def apply_modifiers_to_image(image: Image.Image,
                             monochrome: bool = False,
                             invert: bool = False,
                             contrast: float = 1) -> Image.Image:
    image = ImageEnhance.Contrast(image).enhance(contrast)

    if monochrome:
        image = image.convert("L")

    if invert:
        image = ImageOps.invert(image)

    return image


def gen_bricked_image(image: Image.Image,
                      pixel_resolution: int = 40,
                      color_count: int = 5,
                      method_quantize=MethodsQuantize.MEDIAN_CUT) -> Image.Image:
    image_man = image.resize((pixel_resolution, pixel_resolution), resample=Image.ADAPTIVE)

    image_man = image_man.quantize(colors=color_count, method=method_quantize)

    image_man = image_man.resize(image.size, resample=Image.NEAREST)

    return image_man
