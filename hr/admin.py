from hr.models import (Organization1, Organization2) 
from django.contrib import admin
from userprofile.models import (UserProfile)

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

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ['user', 'likes_chees', 'favourite_hamster_name']



admin.site.register(Organization1, Organization1Admin)
admin.site.register(Organization2)
admin.site.register(UserProfile, UserProfileAdmin)