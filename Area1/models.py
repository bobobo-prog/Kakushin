from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Prof(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	qualifications = models.CharField(max_length=10000)
	image = models.URLField(default=None,null=True)
	



	def __str__(self):
		return self.name	



class Review(models.Model):
	prof = models.ForeignKey(Prof,on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	body = models.TextField()
	posted_on = models.DateTimeField(default = timezone.now)
	active = models.BooleanField(default=False)


	class Meta:
		ordering = ['posted_on']

	def __str__(self):
		return 'Review {} by {}'.format(self.body,self.name)


