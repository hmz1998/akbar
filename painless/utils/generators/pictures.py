"""
Generate a random image using PIL.
"""
import os

from PIL import Image, ImageDraw, ImageFont
from django.conf import settings

from kernel.settings.base import BASE_DIR


def pic_exist(width, height, file_name=None, *args, **kwargs):
    if file_name:
        path = os.path.join('media/upload/fake/', f'{file_name}_{width}X{height}.png')
    else:
        path = os.path.join('media/upload/fake/', f'{width}X{height}.png')
    return os.path.exists(path)


def dir_exist(dir_name):
    return os.path.exists(os.path.join(BASE_DIR, 'media/upload/', dir_name))


def make_dir(dir_name):
    path = os.path.join(BASE_DIR, 'media/upload/', dir_name)
    os.mkdir(path)


def pic_producer(width, height, message=None, prefix=None, *args, **kwargs):
    if prefix:
        path = os.path.join(BASE_DIR, 'media/upload/fake/', f'{prefix}_{width}X{height}.png')
    else:
        path = os.path.join(BASE_DIR, 'media/upload/fake/', f'{width}X{height}.png')
        # path = os.path.join('../../../media/upload/fake/', f'{width}X{height}.png')

    if not dir_exist('fake'):
        make_dir('fake')

    if not pic_exist(prefix, width, height):
        if message:
            msg = message
        else:
            msg = f'{width} X {height}'

        img = Image.new('RGB', (width, height), color=(204, 204, 204))
        draw = ImageDraw.Draw(img)
        txt_width, txt_height = draw.textsize(msg)
        draw.text(((width - txt_width) / 2, (height - txt_height) / 2), msg, fill=(165, 165, 165))

        img.save(path)


if __name__ == "__main__":
    pic_producer(1024, 728, )
