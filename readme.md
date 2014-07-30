
### Instructions on how to set up GeoDjango with count data

[From GeoDjango instructions](https://docs.djangoproject.com/en/dev/ref/contrib/gis/install/postgis/#spatialdb-template)

Install postgis
````shell
## postgis location when installed with hombrew
brew install postgis

## Install requirements
pip install -r requirements.txt

## Set up template DB (may have installed postgis in a different place)
POSTGIS_SQL_PATH=/usr/local/Cellar/postgis/2.1.1/share/postgis/

## Creating the template spatial database.
createdb -E UTF8 template_postgis
createlang -d template_postgis plpgsql # Adding PLPGSQL language support.

## Allows non-superusers the ability to create from this template
psql -d postgres -c "UPDATE pg_database SET datistemplate='true' WHERE datname='template_postgis';"

## Loading the PostGIS SQL routines
psql -d template_postgis -f $POSTGIS_SQL_PATH/postgis.sql
psql -d template_postgis -f $POSTGIS_SQL_PATH/spatial_ref_sys.sql

## Enabling users to alter spatial tables.
psql -d template_postgis -c "GRANT ALL ON geometry_columns TO PUBLIC;"
psql -d template_postgis -c "GRANT ALL ON geography_columns TO PUBLIC;"
psql -d template_postgis -c "GRANT ALL ON spatial_ref_sys TO PUBLIC;"

## From https://docs.djangoproject.com/en/dev/ref/contrib/gis/tutorial/#setting-up
createdb -T template_postgis geodjango

## Shouldn't need to do these steps if cloning the project
# django-admin.py startproject geodjango
# cd geodjango && python manage.py startapp county
````

Next, edit settings.py and add db configuration files, in `settings.py` add your db configuration:
````python
DATABASES = {
    'default': {
         'ENGINE': 'django.contrib.gis.db.backends.postgis',
         'NAME': 'geodjango',
         'USER': 'scott',
     }
}
````

Set up your python app

````shell
# Migrate the db
python manage.py syncdb
# Download the county shape data
mkdir county/data && cd county/data
wget http://www2.census.gov/geo/tiger/TIGER2013/COUNTY/tl_2013_us_county.zip && unzip tl_2013_us_county.zip
# Load the django shell
python manage.py shell
````

In python shell - import your data
````python
from county import load
load.run() # Will load all the counties

# Run a query on the county data
from county.models import CountyBorder
pnt = 'POINT(-122.422264 37.762309)'
CountyBorder.objects.filter(mpoly__contains=pnt)
```