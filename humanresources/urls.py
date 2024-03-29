from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()                        

urlpatterns = patterns('',
    (r'^hrs/', include('hr.urls')),
    (r'^accounts/', include('userprofile.urls')),
    # Examples:
    # url(r'^hello/$', 'hr.views.hello'),
    # url(r'^hello_template/$', 'hr.views.hello_template'),
    # url(r'^$', 'humanresources.views.home', name='home'),
    # url(r'^humanresources/', include('humanresources.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
url(r'^report_builder/', include('report_builder.urls')),
url(r'^admin/', include(admin.site.urls)),

url(r'^accounts/login/$',	'humanresources.views.login'),
url(r'^accounts/auth/$',	'humanresources.views.auth_view'),
url(r'^accounts/logout/$',	'humanresources.views.logout'),
url(r'^accounts/loggedin/$',	'humanresources.views.loggedin'),
url(r'^accounts/invalid/$',	'humanresources.views.invalid_login'),

)
