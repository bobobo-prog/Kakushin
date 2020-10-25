from Users.models import Document
from django.shortcuts import render,redirect
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm,UploadForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage


def register(request):
	if (request.method=="POST"):
		form = UserRegisterForm(request.POST)
		if (form.is_valid()):
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request,f'Account created for {username} , You can Log In now !')
			return redirect('login')

	else:
		form = UserRegisterForm()
	return render(request,'Users/register.html',{'form':form})

@login_required
def profile(request):
	if request.method == "POST":
		u_form = UserUpdateForm(request.POST,instance=request.user)
		p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)

		if u_form.is_valid and p_form.is_valid:
			u_form.save()
			p_form.save()
			messages.success(request,f'Your account has been Updated!')
			return redirect('Users-profile')
	else:
		u_form = UserUpdateForm()
		p_form = ProfileUpdateForm()


	context = {'u_form':u_form,
				'p_form':p_form}
	return render(request,'Users/profile.html',context)

@login_required
def show_list(request):
	
	form = UploadForm(request.POST,request.FILES)

	documents = Document.objects.filter(user = request.user)


	context = {'documents':documents,'form':form}
	return render(request,'Users/List.html',context)


@login_required
def prof_upload(request):
	if request.method == 'POST':
		form = UploadForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
	else:
		form = UploadForm()

	return render(request,'Users/upload.html',{'form':form})




