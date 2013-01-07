from dataconverters import kml
from geojson import dumps

class TestKMLfile:

    def test_kmlfile(self):
        path = 'testdata/kml/AngolaTelecoms.kml'
        with open(path) as stream:
            iterator, metadata = kml.parse(stream)
            print iterator

