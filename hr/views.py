from django.shortcuts import render_to_response 
from hr.models import Organization1
from django.http import HttpResponse
# Create your views here.

def hrs(request):
	language = 'en-us'
	session_language = 'en-us'

	if 'lang' in request.COOKIES:
		language = request.COOKIES['lang']

	if 'lang' in request.session:
		session_language = request.session['lang']

	return render_to_response('hrs.html',
					  		 {'hrs': Organization1.objects.all(),
					  		  'language': language,
							  'session_language': session_language})

def hr(request, hr_id=1):
	return render_to_response('hr.html',
					  		 {'hr': Organization1.objects.get(id=hr_id)})

def language(request, language='en-us'):
	response = HttpResponse("setting language to %s" % language)

	response.set_cookie('lang', language)

	request.session['lang'] = language

	return response