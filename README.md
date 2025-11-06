# COMP3005A3

COMP 3005 Fall 2025
Cal McLelland
Assignment 3

---------------------------------------
-- Installation (Windows PowerShell) --
---------------------------------------

------------
-- Python --
------------

winget install --id Python.Python.3 -e --source winget

----------------
-- SQLAcademy --
----------------

py -3 -m pip install sqlalchemy psycopg[binary] psycopg2

---------------------
-- Create Database --
---------------------

winget install --id PostgreSQL.PostgreSQL -e <- TODO: fix this

Start-Service postgresql-x64-17

Get-Service *postgres*

psql -U postgres

CREATE USER calmclelland WITH PASSWORD 'password123';
CREATE DATABASE student OWNER calmclelland;
\q