from django.shortcuts import render_to_response
from django.http import httpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf

def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html', c)


def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return httpResponseRedirect('/accounts/loggedin')
	else:
		return httpResponseRedirect('/accounts/invalid')