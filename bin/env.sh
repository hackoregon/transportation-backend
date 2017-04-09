#! /bin/bash

# In order to configure your environment for building Docker images, you
# must source this file in the shell where you will build the image.
# For example:
#   $ source ./build_proj/bin/env.sh
export PROJ_SETTINGS_DIR=transDjango # This sets up access for other scripts to the app's subdirectory
export DOCKER_IMAGE=transport-service # This is used to identify the service being run by test-proj.sh

echo "##############################"
echo  LOCAL CONFIG SETTINGS
echo "##############################"
echo  PROJ_SETTINGS_DIR $PROJ_SETTINGS_DIR
echo  DOCKER_IMAGE $DOCKER_IMAGE
