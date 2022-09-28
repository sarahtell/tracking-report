# TRACKING REPORT

## Table of contents
* [General information](#generalinfo)
* [Technologies](#tech)
* [Build](#build)
* [Run](#run)
* [Test](#test)

## General information
This program is used to generate a report for a tracking pixel solution. The input to the program is a date-range and a file path to a log-file containing visit information from an arbitrary number of websites. A report showing the number of page views and unique visitors on each website is generated as output. 

## Technologies
* Pyhton
* pytest

## Build
To build this program, do the following steps: 
* clone this repo

In the command line, head to the root and write the following commands: 
* python3 -m venv env
* source env/bin/activate
* pip3 install -r requirements.txt

## Run
The program runs as a command line tool which requires the start and end dates of the time range, as well as the path to the log-file as input.

The following command will start the program: 
* PYTHONPATH=./src python3 main.py --startdate "YYYY-MM-DD HH:MM:SS" --enddate "YYYY-MM-DD HH:MM:SS" --filepath <file_path>

## Test
To run all the tests in the test folder, write the following command:
* PYTHONPATH=./src pytest test/
