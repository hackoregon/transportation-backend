# Local deployment on Ubuntu 16.04 LTS workstation

1. `cd ubuntu-local-deploy`.
2. `./1install-database-gis-services`. This installs all the Ubuntu packages you'll need. It will pause for you to approve adding the UbuntuGIS PPA - press `Enter` when it does. This installer is my GIS services stack; there's more here than we'd need for a server but it's fine on a desktop. Please open an issue if anything here conflicts with what you've got installed!

     The script will add you as a PostgreSQL superuser with your user ID, so you can connect via the Unix socket using peer authentication without a password. It will also create a database for you with the same name as your user ID and create all the PostGIS extensions in it. If these operations have already been done it will throw errors that you can ignore. 

    After creating the database, the script will create a database schema document via `postgresql_autodoc` in `<your-user-id>.html`. Then it will restore the geocoder database. This takes a while; it downloads a PostgreSQL `pgdump` file and restores it. Finally it will create a database schema document `geocoder.html'.
3. `./2provision`. This creates the `venv` virtual environment, installs Django in it and then creates the `transdev` PostgreSQL role / database.
4. `./3populate-database`. This populates the database and documents the schema to `transDjango/transdev.html`. This also takes a while.
5. `./4start-server`. This starts the server listening on `localhost:8000`.
postgis.list

## Sample APIs

To test: Start the server: `cd ubuntu-local-deploy; ./4start-server`. Then right-click on one of the endpoints below and open in a new tab.

All Features - warning: this takes a couple of minutes!<br>
<http://localhost:8000/transport/features>

Single Features:<br>
<http://localhost:8000/transport/features/1>

Features can be filtered by source name:<br>
<http://localhost:8000/transport/features?source_name=Grind%20and%20Pave>

Conflict data can be used with or without minimum date(days) and distance(meters) query params.  Default is 14 days and 100 meters.<br>
<http://localhost:8000/transport/conflicts?days=7&distance=200>

A address can be provided to find nearby projects.  Required query params are 'address' and 'date'.  Optional params are 'days' and 'distance'.<br>
<http://localhost:8000/transport/nearby?address=321%20NW%20Glisan%20Ave,%20Portland,%20OR&date=2016-03-03&distance=500&days=20>

### Current imported data

The ingest_jsons importer will imports Point, Lines and Polygons for CIP and Street Permit city APIs.  The street permit data is being loaded as a place holder for something more interesting/useful.  But it does allow us to provide two different project types to query for on the front end.  

The ingest_csvs importer will import geocoded Point data. For now, this data orginates from Ed's geocoder.  Examine the generated CSV files in APIimports/management/commands/datafiles/ for more detail about how they're formatted. This data is a bit "customized" for now, as they were imported from City-sourced PDFs or Excel spreadsheets, cleaned to work in the geocoder, and cleaned again for the output.  

The ingest_local_jsons will load geojson that was converted from City of Portland shapefiles in QGIS. For now, ingest_local_jsons will only ingest valid geojson files.

### Create Your Own Import Script

Any GeoJson data can be imported by the current ingest_jsons script.  One possible procedure for adding a data set:

1. Add the GeoJson to the database by copying/modifying the APIimports/management/command/import_jsons.py script.
2. Add the appropriate metadata to the APIimports/constants file.
3. Add the API name to the APIimports/management/command/injest_jsons.py script.
