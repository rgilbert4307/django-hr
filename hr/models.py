from django.db import models

class Organization1(models.Model):
	fullname = models.CharField(max_length=100)
	citizenship = models.CharField(max_length=50)
	dateofbirth = models.DateField()
	address = models.CharField(max_length=200)
	city = models.CharField(max_length=30)
	country = models.CharField(max_length=30)
	postalcode = models.IntegerField()
	martialstatus = models.CharField(max_length=30)
	homephone = models.IntegerField()
	mobile = models.IntegerField()
	primaryemail = models.CharField(max_length=70)
	alternateemail = models.CharField(max_length=70)
	startingdate = models.DateField()
	position = models.CharField(max_length=100)
	empstatus = models.CharField(max_length=70)

	emergncpointofcontact = models.CharField(max_length=100)
	emergncaddress = models.CharField(max_length=200)
	emergnccity = models.CharField(max_length=30)
	emergnccountry = models.CharField(max_length=30)
	emergncpostalcode = models.IntegerField()
	emergncreleationship = models.CharField(max_length=30)
	emergncmobile = models.IntegerField()

	bankname = models.CharField(max_length=100)
	bankaccount = models.IntegerField()
	salary = models.FloatField()

	def __unicode__(self):
		return self.fullname

class Organization2(models.Model):
	fullname = models.CharField(max_length=100)
	citizenship = models.CharField(max_length=50)
	dateofbirth = models.DateField()
	address = models.CharField(max_length=200)
	city = models.CharField(max_length=30)
	country = models.CharField(max_length=30)
	postalcode = models.IntegerField()
	martialstatus = models.CharField(max_length=30)
	homephone = models.IntegerField()
	mobile = models.IntegerField()
	primaryemail = models.CharField(max_length=70)
	alternateemail = models.CharField(max_length=70)
	startingdate = models.DateField()
	position = models.CharField(max_length=100)
	empstatus = models.CharField(max_length=70)

	emergncpointofcontact = models.CharField(max_length=100)
	emergncaddress = models.CharField(max_length=200)
	emergnccity = models.CharField(max_length=30)
	emergnccountry = models.CharField(max_length=30)
	emergncpostalcode = models.IntegerField()
	emergncreleationship = models.CharField(max_length=30)
	emergncmobile = models.IntegerField()

	bankname = models.CharField(max_length=100)
	bankaccount = models.IntegerField()
	salary = models.FloatField()

	def __unicode__(self):
		return self.fullname