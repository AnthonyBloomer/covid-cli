import csv
import time
from datetime import datetime

from prettytable import PrettyTable

from .api import countries, country, totals, us_states


def to_csv(data):
    fieldnames = set()
    for event in data:
        fieldnames |= event.keys()
    with open("%s.csv" % int(time.time()), "w", newline="") as c:
        w = csv.DictWriter(c, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(data)


def calculate_death_rate(deaths, recovered):
    if recovered == 0:
        return "N/A"
    return str(round(100 * deaths / (deaths + recovered))) + "%"


def from_timestamp(updated):
    return datetime.fromtimestamp(updated / 1000).strftime("%Y-%m-%d %H:%M")


def create_table(args):
    if args.country:
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
        json = country(args.country)
        x.add_row(
            [
                json["country"],
                json["deaths"],
                json["critical"],
                json["cases"],
                json["recovered"],
                calculate_death_rate(json["deaths"], json["recovered"]),
                from_timestamp(json["updated"]),
            ]
        )
        print(x)
        if args.csv:
            to_csv(json)
    elif args.totals:
        x = PrettyTable()
        x.field_names = [
            "Active",
            "Cases",
            "Deaths",
            "Recovered",
            "Death Rate",
            "Updated",
        ]
        json = totals()
        x.add_row(
            [
                json["active"],
                json["cases"],
                json["deaths"],
                json["recovered"],
                calculate_death_rate(json["deaths"], json["recovered"]),
                from_timestamp(json["updated"]),
            ]
        )

        print(x)
        if args.csv:
            to_csv(json)
        return True
    elif args.all:
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
        c = countries(args.sort_by)
        for d in c:
            x.add_row(
                [
                    d["country"],
                    d["active"],
                    d["cases"],
                    d["deaths"],
                    d["recovered"],
                    calculate_death_rate(d["deaths"], d["recovered"]),
                    from_timestamp(d["updated"]),
                ]
            )
        print(x)
        if args.csv:
            to_csv(c)
        return True
    elif args.us:
        x = PrettyTable()
        x.field_names = [
            "State",
            "Active",
            "Cases",
            "Deaths",
        ]
        states = us_states(sort_by=args.sort_by)
        for state in states:
            x.add_row(
                [state["state"], state["active"], state["cases"], state["deaths"],]
            )
        print(x)
        if args.csv:
            to_csv(states)
        return True
    else:
        return False
