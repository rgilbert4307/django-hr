from django.shortcuts import render_to_response 
from hr.models import Organization1
# Create your views here.

def hrs(request):
	return render_to_response('hrs.html',
					  		 {'hrs': Organization1.objects.all()})

def hr(request, hr_id=1):
	return render_to_response('hr.html',
					  		 {'hr': Organization1.objects.get(id=hr_id)})