from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	likes_chees = models.BooleanField()
	favourite_hamster_name = models.CharField(max_length=50)
	def __unicode__(self):
		 return u"%s" % (self.user)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])