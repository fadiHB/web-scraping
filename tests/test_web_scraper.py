from web_scraper import __version__
from web_scraper.web_scraper import get_citations_needed_count,get_citations_needed_report
import requests
from bs4 import BeautifulSoup

def test_version():
    assert __version__ == '0.1.0'


def test_get_citations_needed_count():
    actual  = get_citations_needed_count('https://en.wikipedia.org/wiki/History_of_Mexico')
    expected = 5
    assert actual == expected
