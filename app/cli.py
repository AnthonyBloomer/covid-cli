import sys
from argparse import ArgumentParser
from datetime import datetime

import requests
from prettytable import PrettyTable

parser = ArgumentParser(prog="covid")
parser.add_argument(
    "-all", "-a", help="Get all countries totals", action="store_true"
)
parser.add_argument(
    "-country", "-c", help="Get a specific country's totals.", default=None
)
parser.add_argument(
    "-totals",
    "-t",
    help="Get global stats: cases, deaths, recovered, time last updated, and active cases",
    action="store_true",
)
parser.add_argument(
    "-sort-by",
    "-s",
    help="Sort data by column.",
    choices=["Country", "Active", "Cases", "Deaths", "Recovered", "Death Rate"],
    default=None,
    nargs="?",
)

args = parser.parse_args()


def calculate_death_rate(deaths, recovered):
    try:
        return str(round(100 * deaths / (deaths + recovered))) + "%"
    except ZeroDivisionError:
        return "0%"


def fromtimestamp(updated):
    return datetime.fromtimestamp(updated / 1000).strftime("%Y-%m-%d %H:%M")


def statistics_for_country(country):
    x = PrettyTable()
    x.field_names = [
        "Country",
        "Deaths",
        "Critical",
        "Cases",
        "Recovered",
        "Death Rate",
        "Updated",
    ]

    req = requests.get("https://corona.lmao.ninja/countries/%s" % country)

    if req.status_code == 404:
        sys.exit("Country not found or doesn't have any cases")

    json = req.json()
    x.add_row(
        [
            json["country"],
            json["deaths"],
            json["critical"],
            json["cases"],
            json["recovered"],
            calculate_death_rate(json["deaths"], json["recovered"]),
            fromtimestamp(json["updated"]),
        ]
    )
    print(x)
    return True


def all_countries():
    x = PrettyTable()
    x.field_names = [
        "Country",
        "Active",
        "Cases",
        "Deaths",
        "Recovered",
        "Death Rate",
        "Updated",
    ]

    req = requests.get("https://corona.lmao.ninja/countries")

    if not req.ok:
        req.raise_for_status()

    json = req.json()

    for country in json:
        x.add_row(
            [
                country["country"],
                country["active"],
                country["cases"],
                country["deaths"],
                country["recovered"],
                calculate_death_rate(country["deaths"], country["recovered"]),
                fromtimestamp(country["updated"]),
            ]
        )
    x.sortby = args.sort_by
    x.reversesort = True
    print(x)
    return True


def totals():
    x = PrettyTable()
    x.field_names = ["Active", "Cases", "Deaths", "Recovered", "Death Rate", "Updated"]

    req = requests.get("https://corona.lmao.ninja/all")

    if not req.ok:
        req.raise_for_status()

    json = req.json()

    x.add_row(
        [
            json["active"],
            json["cases"],
            json["deaths"],
            json["recovered"],
            calculate_death_rate(json["deaths"], json["recovered"]),
            fromtimestamp(json["updated"]),
        ]
    )

    print(x)
    return True


def main():
    if args.country:
        statistics_for_country(args.country)
    elif args.totals:
        totals()
    elif args.all:
        all_countries()
    else:
        parser.print_help()
        sys.exit(0)
        
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
   
