from codeschool import models
from cs_questions.models import CodingIoResponse, Question
from cs_auth.models import FriendshipStatus
# Create your models here.

class HelpSession(models.Model):
    response = models.ForeignKey(CodingIoResponse)
    question = models.ForeignKey(Question)
    owner = models.ForeignKey(models.User,related_name="help_sessions_as_owner")
    helper = models.ForeignKey(models.User,related_name="help_sessions_as_helper")
    comment = models.TextField()
    created = models.DateField(auto_now_add=True) 

class LineComment(models.Model):
    help_session = models.ForeignKey(HelpSession,related_name="comments_on_line")
    commment = models.TextField()
    
