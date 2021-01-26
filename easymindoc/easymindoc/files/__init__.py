from .annex import Annex
from .image import Image
from .video import Video

def read_uri(obj, line):
    return obj.read_uri(line)