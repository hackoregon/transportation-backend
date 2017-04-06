"""
Ingest HackOR geocoded data in .csv format to transdev database 
"""

import csv
import json


with open('../management/commands/datafiles/tidy_geocoder_output.csv', mode='r') as infile:
    reader = csv.DictReader(infile)
    data = list(reader)

print(data)



#with open('output.json', mode='w') as outfile:
#    writer = csv.writer(outfile)
#    json.dump(data, outfile)