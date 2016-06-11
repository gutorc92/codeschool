from django.shortcuts import render
from .models import HelpSession
import srvice

# Create your views here.
@srvice.api
def friendhelper(request, friend_pk, reponse_pk, question_pk):
	hpSession = HelpSession()
	hpSession.owner	= request.user 
	hpSession.helper = friend_pk
	hpSession.question = question_pk
	hpSession.response = response_pk
	hpSession.save()
	return None


