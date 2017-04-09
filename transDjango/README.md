## Django app for loading data (and serving APIs?)

This particular setup uses a management command (e.g. `manage.py <loader_name>)` to do the uploads.  A few notes:

* The test was run on a mac and Ubuntu 14.04 LTS with a local DB.  We've not tried to push to the remote DB yet.
* Someone who knows something about geospatial databases may have some opinions on projections, database setup, etc...  These opinions, and any others, would be most welcome.


### Mac Installation (also works on Ubuntu 14.04 LTS)

You will need a Postgres database with PostGIS installed and it's assumed you can log into postres as a superuser.  If you don't use homebrew, you will need to use a alternate method of installing gdal and libgeoip.

At the command line:
```
git clone https://github.com/hackoregon/transportation-backend.git
cd transportation-backend
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
brew install gdal
brew install libgeoip
psql postgres
```
    
(Now in Postgres...)
```
CREATE ROLE transdev WITH PASSWORD 'password' LOGIN;
CREATE DATABASE transdev WITH OWNER=transdev;
\c transdev
CREATE EXTENSION postgis;
\q
```

(Back at the command line...)

Enable local settings. 

```
mv transDjango/transDjango/settings_local_example.py transDjango/transDjango/settings_local.py
```

Create the database structure
```
cd transDjango
./manage.py migrate
./manage.py createcachetable
```

Download API json files to the database

`./manage.py import_jsons`

Copy data to the main geometry tables that are connected to the API

`./manage.py ingest_jsons`

Convert local CSV data into geojson and load them to the main geometry tables

`./manage.py ingest_csvs`

Run the dev server and see if the API is working

`./manage.py runserver`

API should be available at 

localhost:8000/api/features

### Current imported data

The ingest_jsons importer will imports Point, Lines and Polygons for CIP and Street Permit city APIs.  The street permit data is being loaded as a place holder for something more interesting/useful.  But it does allow us to provide two different project types to query for on the front end.  

The ingest_csvs importer will import geocoded Point data. For now, this data orginates from Ed's geocoder.  Examine the generated CSV files in APIimports/management/commands/datafiles/ for more detail about how they're formatted. This data is a bit "customized" for now, as they were imported from City-sourced PDFs or Excel spreadsheets, cleaned to work in the geocoder, and cleaned again for the output.  

### Create Your Own Import Script

Any GeoJson data can be imported by the current ingest_jsons script.  One possible procedure for adding a data set:

1. Add the GeoJson to the database by copying/modifying the APIimports/management/command/import_jsons.py script.
2. Add the appropriate metadata to the APIimports/constants file.
3. Add the API name to the APIimports/management/command/injest_jsons.py script.