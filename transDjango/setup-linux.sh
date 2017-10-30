#! /bin/bash

# USAGE:
# $ chmod +x setup-linux.sh
# $ ./setup-linux.sh
#
# OR:
# $ bash setup-linux.sh

# below steps copied originally from transportation-backend/transDjango/README.md 
# see: https://github.com/hackoregon/transportation-backend/blob/master/transDjango/README.md

# if this script is executing then we are already inside of a working copy tree cloned from the repo
#git clone https://github.com/hackoregon/transportation-backend.git
#cd transportation-backend

# install apt packages missing from a clean Linux Mint 18.2 install
sudo apt-get install -y virtualenv libpq-dev python3-dev postgresql-contrib

# create and activate a virtualenv
virtualenv -p python3 venv
source venv/bin/activate

# install python module requirements into virtualenv
pip install -r requirements.txt

# MacOS Homebrew packages?
#brew install gdal
#brew install libgeoip

# install equivalent apt packages for Debian/Ubuntu/Mint systems
sudo apt-get install -y gdal-bin libgeoip1

# this command fails on my system
#psql postgres
