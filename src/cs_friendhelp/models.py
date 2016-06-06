from codeschool import models
from cs_questions.models import CodingIoResponse
from cs_auth.models import FriendshipStatus
# Create your models here.

class HelpSession(models.Model):
    response = models.ForeignKey(CodingIoResponse)
    owner = models.ForeignKey(models.User,related_name="help_sessions_as_owner")
    helper = models.ForeignKey(models.User,related_name="help_sessions_as_helper")
    comment = models.TextField()

class LineComment(models.Model):
    help_session = models.ForeignKey(HelpSession,related_name="comments_on_line")
    commment = models.TextField()
    
