from aloe import step,world
from codeschool import models

@step(r'System create user "(.*)"')
def create_user(step,name):
	user = models.User(username=name,email="teste@teste.com")
	user.set_password("teste")
	user.save()

@step(r'System create user "(.*)" with password "(.*)"')
def create_user(step,name, password):
	user = models.User(username=name,email="teste@teste.com")
	user.set_password(password)
	user.save()

