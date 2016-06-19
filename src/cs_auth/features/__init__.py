from aloe import step,world
from cs_core.steps.steps import create_user,check_permissions
import cs_core.steps.browser 

@step(r'I access "(.*)"')
def access_url(step,url):
	world.fb = url

@step(r'I see "(.*)"')
def see(step,url):
	assert world.fb == url
