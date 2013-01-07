from fastkml import kml

def parse(stream, **kwargs):
    k = kml.KML()
    kmlstring = stream.read()
    k.from_string(kmlstring)

    def iterate(k):
        foo = []
        for item in k:
            if isinstance(item, kml.Document) or isinstance(item, kml.Folder):
                foo.append({item: iterate(item.features())})
            else:
                foo.append(item)
        return foo

    return iterate(k.features()), {}

