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

   usage: covid [-h] [-all] [-country COUNTRY] [-totals] [-csv] [-us]
                [-sort-by [{Country,Active,Cases,Deaths,Recovered,Death Rate}]]

   optional arguments:
     -h, --help            show this help message and exit
     -all, -a              Get all countries totals
     -country COUNTRY, -c COUNTRY
                           Get a specific country's totals.
     -totals, -t           Get global stats: cases, deaths, recovered, time last
                           updated, and active cases
     -csv                  Set this flag to output to CSV.
     -us, -u               Get United States data.
     -sort-by [{Country,Active,Cases,Deaths,Recovered,Death Rate}], -s [{Country,Active,Cases,Deaths,Recovered,Death Rate}]
                           Sort data by column.

Demo
----

|asciicast|

.. |asciicast| image:: https://asciinema.org/a/315090.svg
   :target: https://asciinema.org/a/315090
