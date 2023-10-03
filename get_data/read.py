# -*- coding: utf-8 -*-
"""File for reading data."""

from pathlib import Path
import logging
import pandas


def read_cvs(path: Path = "/data/unemployment/europe_unemployment_rate.csv"):
    """File for reading data.
    :param Path path: path to file europe_unemployment_rate.csv if not changed
    :rtype None:
    """
    data = pandas.read_csv(path)
    return data
