from aloe import step,world
from codeschool import models

@step(r'System create user "(.*)"')
def create_user(step,name):
	user = models.User(username=name,password="Teste")
	user.save()


