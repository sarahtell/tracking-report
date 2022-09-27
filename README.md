# TRACKING REPORT

## Table of contents
* [General information](#generalinfo)
* [Technologies](#tech)
* [Build](#build)
* [Run](#run)
* [Test](#test)
* [Delimitations](#delim)

## General information
This program generates a report for a tracking pixel solution. The input to the program is a date-range and a file path to a log-file containing visit information from an arbitrary number of websites. A report showing the number of page views and unique visitors on each website is generated as output. 

## Technologies
* Pyhton
* pytest

## Build

## Run
The program run as a command line tool which requires the start and end dates of the time range, as well as the path to the log-file as input.

The following command will start the program: python3 main.py --startdate "YYYY-MM-DD HH:MM:SS" --enddate "YYYY-MM-DD HH:MM:SS" --filepath <file_path>

## Test

## Delimitations
This program is subject to some delimitations, as follows: 

* A