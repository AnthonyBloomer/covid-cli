covid-cli
=========

   Get the latest COVID-19 information via the command line.

Installation
------------

::

   pip install covid-cli

Usage
-----

::

   usage: covid [-h] [-all] [-country COUNTRY] [-totals]
                [-sort-by [{Country,Active,Cases,Deaths,Recovered,Death Rate}]]

   optional arguments:
     -h, --help            show this help message and exit
     -all, -a              Get all countries totals
     -country COUNTRY, -c COUNTRY
                           Get a specific country's totals.
     -totals, -t           Get global stats: cases, deaths, recovered, time last
                           updated, and active cases
     -sort-by [{Country,Active,Cases,Deaths,Recovered,Death Rate}], -s [{Country,Active,Cases,Deaths,Recovered,Death Rate}]
                           Sort data by column.
