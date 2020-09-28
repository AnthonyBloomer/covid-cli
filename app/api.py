import requests

BASE_URL = "https://disease.sh"
API_VERSION = "v3"


def make_request(url, params=None):
    req = requests.get(url, params=params)
    if not req.ok:
        req.raise_for_status()
    json = req.json()
    return json


def countries(sort_by):
    params = {"sort": sort_by}
    return make_request(
        "%s/%s/covid-19/countries" % (BASE_URL, API_VERSION), params=params
    )


def country(name):
    return make_request("%s/%s/covid-19/countries/%s" % (BASE_URL, API_VERSION, name))


def totals():
    return make_request("%s/%s/covid-19/all" % (BASE_URL, API_VERSION))


def us_states(sort_by):
    params = {"sort": sort_by}
    return make_request(
        "%s/%s/covid-19/states" % (BASE_URL, API_VERSION), params=params
    )
