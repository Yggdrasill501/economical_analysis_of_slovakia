# -*- coding: utf-8 -*-
"""File for downloading data from Eurostat."""
import eurostat
import scrapy


class DownloadData:
    """Class for downloading data from Eurostat."""
    def __init__(self,
                 economic_activity_code: str ='',
                 energy_inflation_code: str = '',
                 food_inflation_code: str = '',
                 gdp_growth_code: str = '',
                 house_price_growth_code: str = '',
                 inflation_rate_code: str = '',
                 population_code: str = '',
                 unemployment_rate_code: str = '') -> None:
        """Constructor.
        :param economic_activity_code: code for economic activity
        :param energy_inflation_code: code for energy inflation
        :param food_inflation_code: code for food inflation
        :param gdp_growth_code: code for GDP growth
        :param house_price_growth_code: code for house price growth
        :param inflation_rate_code: code for inflation rate
        :param population_code: code for population
        :param unemployment_rate_code: code for unemployment rate
        rtype None:
        """
        self.economic_activity_code = economic_activity_code
        self.energy_inflation_code = energy_inflation_code
        self.food_inflation_code = food_inflation_code
        self.gdp_growth_code = gdp_growth_code
        self.house_price_growth_code = house_price_growth_code
        self.inflation_rate_code = inflation_rate_code
        self.population_code = population_code
        self.unemployment_rate_code = unemployment_rate_code
