from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^all/$', 'hr.views.hrs'),
	url(r'^get/(?P<hr_id>\d+)/$', 'hr.views.hr'),
)