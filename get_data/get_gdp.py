# -*- coding: utf-8 -*-
"""File for getting GDP data from World Bank API."""
import scrapy
import json


class GetGDP:
    """File that use webscraping to get GDP data from World Bank API."""
    def __init__(self) -> None:
        """Constructor

        :rtype None:
        """
        self._api = 'http://api.worldbank.org/v2/country/br/indicator/NY.GDP.MKTP.CD?format=json'
        self._url = scrapy.Request(self._api)
        self._data = scrapy.urlopen(self._url).read()
        self._gdp = json.loads(self._data)

    def get_data(self) -> None:
        """Get data from World Bank API.

        :rtype None:
        """
        print(self._gdp)
        return self._gdp
