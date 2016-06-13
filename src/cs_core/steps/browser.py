from contextlib import contextmanager

import aloe_webdriver
from aloe_webdriver.django import visit_page 
from aloe import around, world
from selenium import webdriver

@around.all
@contextmanager
def with_browser():
    world.browser = webdriver.Firefox()
    yield
    world.browser.quit()
    delattr(world, 'browser')
