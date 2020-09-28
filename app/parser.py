from argparse import ArgumentParser


class Parser:
    def __init__(self):
        self.parser = ArgumentParser(prog="covid")
        self.parser.add_argument(
            "-all", "-a", help="Get all countries totals", action="store_true"
        )
        self.parser.add_argument(
            "-country", "-c", help="Get a specific country's totals.", default=None
        )
        self.parser.add_argument(
            "-totals",
            "-t",
            help="Get global stats: cases, deaths, recovered, time last updated, and active cases",
            action="store_true",
        )
        self.parser.add_argument(
            "-csv", help="Set this flag to output to CSV.", action="store_true",
        )
        self.parser.add_argument(
            "-us", "-u", help="Get United States data.", action="store_true",
        )
        self.parser.add_argument(
            "-sort-by",
            "-s",
            help="Sort data by column.",
            choices=[
                "cases",
                "todayCases",
                "deaths",
                "todayDeaths",
                "recovered",
                "active",
                "critical",
                "casesPerOneMillion",
                "deathsPerOneMillion",
            ],
            default=None,
            nargs="?",
        )

    def parse_args(self):
        return self.parser.parse_args()

    def help(self):
        return self.parser.print_help()
