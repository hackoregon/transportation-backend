CREATE ROLE transdev WITH PASSWORD 'password' LOGIN;
CREATE DATABASE transdev WITH OWNER=transdev;
\c transdev
CREATE EXTENSION postgis;
