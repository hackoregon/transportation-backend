## Django app for loading data (and serving APIs?)

This particular setup uses a management command (e.g. `manage.py <loader_name>)` to do the uploads.  A few notes:

* In order to minimize merge conflicts, each loader is a separate file and loads only one geojson file.  It's possible that this process could be abstracted a little bit though, given the right conditions.  For instance, if we assume that we will be loading all fields from each API, a single loader could potentially serve all APIs.
* The test was run on a mac and Ubuntu 14.04 LTS with a local DB.  We've not tried to push to the remote DB yet.
* Someone who knows something about geospatial databases may have some opinions on projections, database setup, etc...  These opinions, and any others, would be most welcome.


### Mac Installation (also works on Ubuntu 14.04 LTS)

You will need a Postgres database with PostGIS installed and it's assumed you can log into postres as a superuser.  If you don't use homebrew, you will need to use a alternate method of installing gdal and libgeoip.

At the command line:
```
git clone https://github.com/hackoregon/transportation-backend.git test
cd transportation-backend test
git checkout -b djangoImport origin/djangoImport
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
Rename /transDjango/transDajngo/settings_local_example.py to settings_local.py and update that file if needed.


### Running the Example

Assumes you are in the transDjango directory

1.  ./manage.py migrate
2.  ./manage.py import_CIPpoints


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

