import os
from django.contrib.gis.utils import LayerMapping
from models import CountyBorder

county_mapping = {
    'statefp' : 'STATEFP',
    'countyfp' : 'COUNTYFP',
    'countyns' : 'COUNTYNS',
    'geoid' : 'GEOID',
    'name' : 'NAME',
    'namelsad' : 'NAMELSAD',
    'lsad' : 'LSAD',
    'classfp' : 'CLASSFP',
    'mpoly' : 'MULTIPOLYGON',
}

county_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/tl_2013_us_county.shp'))

def run(verbose=True):
    lm = LayerMapping(CountyBorder, county_shp, county_mapping,
                      transform=False, encoding='iso-8859-1')

    lm.save(strict=True, verbose=verbose)