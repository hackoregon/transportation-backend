#! /bin/bash
# Setup Project Specfics - Make sure env.sh is in the .gitignore and .dockerignore
export DOCKER_IMAGE=transport-service
export PROJ_SETTINGS_DIR=transDjango
export DEPLOY_TARGET=integration # it's always dev on your local machine
export CONFIG_BUCKET=hacko-transportation-config
echo "##############################"
echo  Your Local Project Environement
echo "##############################"
echo DOCKER_IMAGE $DOCKER_IMAGE
echo PROJ_SETTINGS_DIR $PROJ_SETTINGS_DIR
echo DEPLOY_TARGET $DEPLOY_TARGET
echo CONFIG_BUCKET $CONFIG_BUCKET
