from fastkml import kml

def parse(stream, **kwargs):
    k = kml.KML()
    kmlstring = stream.read()
    k.from_string(kmlstring)
    return k.features(), {}

