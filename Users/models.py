from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
	user = models.OneToOneField(User,on_delete = models.CASCADE)
	image = models.ImageField(default = 'default.jpg',upload_to='profile_pics')


	def __str__(self):
		return f'{self.user.username} Profile'

	# def save(self):
	# 	super().save()

	# 	img = Image.open(self.image.path)
	# 	r_img = img.convert('RGB')
	# 	if(r_img.height > 300 or r_img.width > 300):
	# 		otp_size = (300,300)

	# 		r_img.thumbnail(otp_size)
	# 		r_img.save(self.image.path)




class Document(models.Model):
	
	def uppath(self,filename):
		return 'documents/uploads/'+str(self.user.username)+'/'+filename

	user = models.ForeignKey(User,on_delete=models.CASCADE)
	docfile = models.FileField(upload_to=uppath)
	#uploaded_at = models.DateTimeField(auto_now_add=True)
	


	def __str__(self):
		return f'{self.user.username}'
	
	




