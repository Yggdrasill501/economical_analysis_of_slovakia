# -*- coding: utf-8 -*-
"""File for getting GDP data from World Bank API."""
import scrapy


class GetGDP:
    """File that use webscraping to get GDP data from World Bank API."""
    def __init__(self) -> None:
        """Constructor

        :rtype None:
        """
        self._api = ''
