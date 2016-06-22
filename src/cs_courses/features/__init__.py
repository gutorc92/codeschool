from aloe import step
from cs_core.steps.steps import *
from codeschool.models import User
from cs_courses.models import Discipline, Course


@step(r'System create discipline "(.*)"')
def create_disciplines(step, name):
  Discipline.objects.create(name=name)

@step(r'System create course "(.*)"')
def create_course(step, name):
  discipline = Discipline.objects.create(name=name)
  teacher = User.objects.first()
  Course.objects.create(discipline=discipline, teacher=teacher)
  
@step(r'System create discipline "(.*)" with courses')
def create_disciplines_with_courses(step, name):
  d = Discipline.objects.create(name=name)
  Course.objects.create(name="c1", discipline=d, teacher=User.objects.first())
  Course.objects.create(name="c2", discipline=d, teacher=User.objects.first())
