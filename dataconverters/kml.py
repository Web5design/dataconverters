from fastkml import kml

def parse(stream, **kwargs):
    k = kml.KML()
    kmlstring = stream.read()
    k.from_string(kmlstring)

    def iterate(k):
        itemlist = []
        for item in k:
            if isinstance(item, kml.Document) or isinstance(item, kml.Folder):
                itemlist.append({item: iterate(item.features())})
            else:
                itemlist.append(item)
        return itemlist

    return iterate(k.features()), {}

