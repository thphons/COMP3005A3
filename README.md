COMP 3005 Fall 2025
Cal McLelland
Assignment 3
Question 1

----------------------------------------------
-- Installation (Windows PowerShell w/ WSL) --
----------------------------------------------

--------------
-- postgres --
--------------

Download and run installer

https://www.postgresql.org/download/windows/

during installation, select "Command Line Tools" to install psql

---------
-- WSL --
---------

wsl --install

------------
-- Python --
------------

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

psql

CREATE DATABASE student;

CREATE ROLE calmclelland WITH LOGIN PASSWORD 'password123';

GRANT ALL PRIVILEGES ON DATABASE student TO calmclelland;

---------
-- Run --
---------

python a3.py

type "help" to view available commands

----------------
-- Demo Video --
----------------

Link to Demo Video

https://mediaspace.carleton.ca/media/COMP3005_A3_Q1_Demo/1_5rrgbp61

