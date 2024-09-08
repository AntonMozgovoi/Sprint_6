import pytest
from selenium import webdriver
from data import Urls


@pytest.fixture(scope='function')
def driver():
    firefox = webdriver.Firefox()
    firefox.get(Urls.MAIN_PAGE)
    firefox.maximize_window()
    yield firefox
    firefox.quit()
