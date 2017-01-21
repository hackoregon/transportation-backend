### Proof of Concept Django GeoJson Loader

This may not be the right way, but it does seem to be *a* way to load data into a PostGIS database using Django.  This particular setup uses a management command (e.g. `manage.py <loader_name>)` to do the deed.  A few notes

* In order to minimize merge conflicts, each loader is a separate file and loads only one geojson file.  It's possible that this process could be abstracted a little bit though, given the right conditions.  For instance, if we assume that we will be loading all fields from each API, a single loader could potentially serve all APIs.
* While roughing this out, I ran into problems loading null values into date fields.  For now, I've simply dropped the date models but this will need to be resolved.
* The test was run on a mac with a local DB.  I've not tried to push to the remote DB yet.
* If we go in this direction, it's assumed that file-based imports will be changed to directly querying the API.
* Someone who knows something about geospatial databases may have some opinions on projections, database setup, etc...  These opinions, and any others, would be most welcome.


## Mac Installation

You will need a Postgres database with PostGIS installed and it's assumed you can log into postres as a superuser.  If you don't use homebrew, you will need to use a alternate method of installing gdal and libgeoip.

At the command line:
```
virtualenv -p python3 venv
source venv/bin/activate
pip install django
pip install django-leaflet
brew install gdal
brew install libgeoip
psql postgres
```
    
(Now in Postgres...)
```
CREATE ROLE transdev WITH PASSWORD 'password';
CREATE DATABASE transdev WITH OWNER=transdev;
/c transdev
CREATE EXTENSION postgis;
\q
```


## Running the example

Assumes you are in the transDjango directory
1.  ./manage.py migrate
2.  ./manage.py import_CIPpoints


## Create Your Own Import Script

To set up a new import script, you will need to do the following:
1. Rename /transDjango/transDajngo/settings_local_example.py to settings_local.py and updated that file if needed.
1. Create the importer script as a management command in APIimports/management/commands.  You can see import_CIPpoints.py for an example.
2. Deposit the relevant GeoJson file in APIimports/management/commands/datafiles
3. Add an import line to the APIimports/models.py file
4. Run the importer at the command line with ./manage.py <your_importer>


