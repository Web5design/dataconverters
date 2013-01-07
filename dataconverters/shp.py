import fiona
import tempfile

def parse(path):
    return fiona.collection(path), {}
