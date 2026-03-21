import os

from django.conf import settings
from PIL import Image


def resize_image(image, new_width=800):
    image_full_path = os.path.join(settings.MEDIA_ROOT, image.name)
    image_pil = Image.open(image_full_path)
    original_width, original_height = image_pil.size

    if original_width <= new_width:
        return image

    new_height = round((new_width * original_height) / original_width)
    new_image = image_pil.resize(
        (new_width, new_height), Image.Resampling.LANCZOS)

    # FIXME: Verificar se está funcionando
    new_image.save(
        image_full_path,
        optimize=True,
        quality=80
    )
    return new_image
