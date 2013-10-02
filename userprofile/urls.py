from django.conf.urls import patterns, include, url

urlpattern = patterns('',
		url(r'^profile/$', 'userprofile.views.user_profile'),
)