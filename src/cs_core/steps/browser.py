from contextlib import contextmanager

import aloe_webdriver
import aloe_webdriver.django
from aloe import around, world, step
from selenium import webdriver

@around.each_example
@contextmanager
def with_browser(scenario,outline,steps):
    world.browser = webdriver.Firefox()
    yield  
    world.browser.quit()
    delattr(world,'browser')  


@step(r'I click in "(.*)"')
def click(scenario, link):
  world.browser.find_element_by_link_text(link).click()
