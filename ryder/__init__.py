from .sources import build
from .articles import read, get_image_from_url


def article(url):
    return read(url)


def source(url):
    return build(url)
