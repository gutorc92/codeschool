from contextlib import contextmanager

import aloe_webdriver
import aloe_webdriver.django
from aloe import around, world
from selenium import webdriver

@around.all
@contextmanager
def with_browser():
    world.browser = webdriver.Firefox()
    yield  
    world.browser.quit()
    delattr(world,'browser')  


