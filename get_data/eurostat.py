# -*- coding: utf-8 -*-
"""File for downloading data from Eurostat."""
import scrapy
import pandas as pd
from pathlib import Path
import logging

MODULE_LOGGER = logging.getLogger(__name__)


class DownloadData:
    """Class for downloading data from Eurostat."""
    def __init__(self,
                 url: str = 'https://ec.europa.eu/eurostat/en/',
                 file_path: Path = "./data") -> None:
        """Constructor."""
        self.url = url
        self.file_path = file_path

    def _download_data(self) -> None:
        """Private method downloads data from Eurostat.

        :rtype None:
        """
