from django.shortcuts import render
import srvice

# Create your views here.
@srvice.api
def friendhelper(request, friend_pk, reponse_pk, question_pk):
	...

	return None


