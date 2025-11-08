COMP 3005 Fall 2025
Cal McLelland
Assignment 3
Question 1

----------------
-- Demo Video --
----------------

Link to Demo Video

https://mediaspace.carleton.ca/media/COMP3005_A3_Q1_Demo/1_5rrgbp61

----------------------------------------------
-- Installation (Windows PowerShell w/ WSL) --
----------------------------------------------

--------------
-- postgres --
--------------

Download and run installer

https://www.postgresql.org/download/windows/

during installation, select "Command Line Tools" to install psql

-- add psql to system path

[Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\Program Files\PostgreSQL\<version>\bin", "User")

where <version> is the version of postgres installed

close and reopen PowerShell

---------
-- WSL --
---------

In PowerShell:

wsl --install

------------
-- Python --
------------

In PowerShell:

wsl -u <username>

sudo apt update
sudo apt install -y python3 python3-venv python3-pip build-essential libpq-dev

-- create a virtual enviroment with venv

python3 -m venv .venv
source .venv/bin/activate

----------------
-- SQLAcademy --
----------------

python -m pip install --upgrade pip setuptools wheel
python -m pip install sqlalchemy psycopg[binary] psycopg2-binary

-------------------------------
-- Create Database (pgadmin) --
-------------------------------

In PowerShell:

psql -h localhost -p 5432 -U postgres

-- enter password for superuser postgres

CREATE ROLE calmclelland WITH LOGIN PASSWORD 'password123';

CREATE DATABASE student OWNER calmclelland;

GRANT ALL PRIVILEGES ON DATABASE student TO calmclelland;

\q

psql -U postgres -d student

ALTER SCHEMA public OWNER TO calmclelland;

\q

---------
-- Run --
---------

python a3.py

type "help" to view available commands


