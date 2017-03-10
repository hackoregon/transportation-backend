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
```

Download API json files to the database

`./manage.py import_jsons`

Copy data to the main geometry tables that are connected to the API

`./manage.py ingest_jsons`

Run the dev server and see if the API is working

`./manage.py runserver`

API should be available at 

localhost:8000/api/points

localhost:8000/api/lines




### Create Your Own Import Script

To set up a new import script, you will need to do the following:
1. Create the importer script as a management command in APIimports/management/commands.  You can see import_CIPpoints.py for an example.
2. Deposit the relevant GeoJson file in APIimports/management/commands/datafiles
3. Add an import line to the APIimports/models.py file
4. Run the importer at the command line with ./manage.py <your_importer>

### Completed Importer Scripts So Far

Notes: So far we're ignoring date/time fields due to some inconsistencies when loading using ogrinspect.

We can always use another set of eyes to make sure things can be abstracted further! 

1. import_CIPpoints.py
2. import_CIPlines.py
3. import_StPJlines.py

