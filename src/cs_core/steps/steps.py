from aloe import step,world
from codeschool import models
from userena.models import UserenaSignup

@step(r'System create user "(.*)"')
def create_user(step,name):
	user = models.User(username=name,email="teste@teste.com")
	user.set_password("teste")
	user.save()

@step(r'System create admin user')
def create_super_user(step):
  user = models.User.objects.create_superuser(username="admin",
                                              email="admin@teste.com",
                                              password="admin")

@step(r'System create user "(.*)" with password "(.*)"')
def create_user(step,name, password):
	user = models.User(username=name,email="teste@teste.com")
	user.set_password(password)
	user.save()

@step(r'System create user "(.*)" with password "(.*)" and email "(.*)"')
def create_user_complete(step,name, password,email):
	user = models.User(username=name)
	user.email= email
	user.set_password(password)
	user.save()

@step(r'System check permissions')
def check_permissions(step):
	UserenaSignup.objects.check_permissions()
