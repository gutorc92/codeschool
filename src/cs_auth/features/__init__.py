from aloe import step,world

@step(r'I access "(.*)"')
def access_url(step,url):
	world.fb = url

@step(r'I see "(.*)"')
def see(step,url):
	assert world.fb == url
