from selene.support.shared import browser
from selene import be, have
import pytest
import uuid


@pytest.fixture()
def setup_responsive_for_window():
    browser.config.window_width, browser.config.window_height = 1800, 1000
    yield


def test_google_finds_selene_successful(setup_responsive_for_window):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))


def test_google_find_unsuccessful():
    uid = uuid.uuid4()
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type(f'{uid}').press_enter()
    browser.element('[id="center_col"]').should(have.text(f'По запросу {uid} ничего не найдено. '))