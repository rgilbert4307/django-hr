from hr.models import (Organization1, Organization2) 
from django.contrib import admin

class Organization1Admin(admin.ModelAdmin):
	list_display = ['fullname',
'citizenship',
'dateofbirth',
'address',
'city',
'country',
'postalcode',
'martialstatus',
'homephone',
'mobile',
'primaryemail',
'alternateemail',
'startingdate',
'position',
'empstatus']

	list_filter = ['fullname']



admin.site.register(Organization1, Organization1Admin)
admin.site.register(Organization2)