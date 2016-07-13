"""
Control authentication and new users registrations.
"""

from django import http
from django.views.generic import TemplateView
from userena.forms import AuthenticationForm
from userena import views
from codeschool.shortcuts import render_html, redirect, render
from codeschool.models import User
from cs_core.forms import SignupForm, SignupOptionalForm
import srvice.decorators 
from .models.profile import FriendshipStatus
from django.core.paginator import Paginator, EmptyPage
from django.core import serializers
import json

class LoginView(TemplateView):
    template_name = 'cs_auth/login.jinja2'

    def get_context_data(self, **kwargs):

        return super().get_context_data(
            signin=AuthenticationForm(),
            signup=SignupForm(),
            signup_opt=SignupOptionalForm(),
            **kwargs
        )

    def post(self, request):
        if request.POST['action'] == 'signup':
            return self.post_signup(request)
        else:
            return self.post_signin(request)

    def post_signin(self, request):
        return views.signin(
                request,
                template_name='cs_auth/login.jinja2',
                extra_context=self.get_context_data(action='signin')
        )

    def post_signup(self, request):
        context = self.get_context_data(action='signup')
        form = SignupForm(request.POST)
        opt_form = SignupOptionalForm(request.POST)

        # Render forms if they are invalid
        if not (opt_form.is_valid() and form.is_valid()):
            context['signup'] = form
            context['signup_opt'] = opt_form
            return super().render_to_response(context)

        # Validate and proceed
        context['signup_opt'] = opt_form
        response = views.signup(
            request,
            signup_form=SignupForm,
            template_name=self.template_name,
            extra_context=context,
            success_url='/',
        )

        # It redirects on success: we intercept and add extra
        # information
        if isinstance(response, http.HttpResponseRedirect):
            # Fill extra info in signup form
            aux = form.cleaned_data
            success_url = '/accounts/%s' % aux['username']
            user = User.objects.get(username=aux['username'])
            user.first_name = aux['first_name']
            user.last_name = aux['last_name']

            # Fill extra profile info
            opt_form = SignupOptionalForm(request.POST)
            opt_form.is_valid()
            aux = opt_form.cleaned_data
            user.profile.about_me = aux['about_me']
            user.profile.gender = aux['gender']
            user.profile.date_of_birth = aux['date_of_birth']

            # Save modifications and go
            user.save()
            user.profile.save()

            return redirect(success_url)
        return response


def index(request):
    if request.user is None:
        return redirect('/accounts/login/')
    else:
        return redirect('/accounts/%s/' % request.user.username)

def friends(request,username):
	user = request.user
	pages = {}
	p = Paginator(user.friends,50);
	pages["friends"] = [p.num_pages,"false", p.object_list]
	p = Paginator(user.colleagues,50)
	pages["colleagues"] = [p.num_pages,"true",p.object_list]
	p = Paginator(user.staff_contacts,50)
	pages["staff"] = [p.num_pages,"true",p.object_list]
	p = Paginator(user.friends_pending,50)
	pages["pending"] = [p.num_pages,"true",p.object_list]
	return render(request,"friends.jinja2",{"user":request.user, "pages": pages})

@srvice.api
def paginatorFriend(request,nrpage,search):
	if (search == "friends"):
		users = request.user.friends
	elif(search == "colleagues"):
		users = request.user.colleagues
	elif(search == "staff"):
		users = request.user.staff_contacts
	elif(search == "pending"):
		users == request.user.friends_pending
	else:
		return None
	if users: 
		paginator = Paginator(users,50);
		try:
			page = paginator.page(nrpage)
		except EmptyPage:
			return "There is no more pages"
		data_total = {}
		for u in page.object_list:
			name = u.first_name + " " + u.last_name
			data = { "pk": u.pk,"name": name, "mugshot": u.profile.get_mugshot_url(), "username": u.username }  	
			data_total[u.username] = data
		print(data_total)
		return data_total
	else:
		return None

@srvice.api
def addFriendshipStatus(request,idowner, idother, status):
	f = FriendshipStatus.objects.filter(owner_id=idowner,other_id=idother)
	of = FriendshipStatus.objects.filter(owner_id=idother,other_id=idowner)
	if not f and of:
		f = FriendshipStatus(owner_id=idowner,other_id=idother)
		f = FriendshipStatus(owner_id=idother,other_id=idowner)
	else:
		f = f[0]
		of = of[0]
	f.status=FriendshipStatus.STATUS_FRIEND
	of.status = FriendshipStatus.STATUS_PENDING
	try:
		f.save()
		of.save()
	except User.DoesNotExist:
		return "User does not exists"
    
	return "Sucefully added friend" 
	

	
