from django.shortcuts import render
from django.http import HttpResponse
from .models import Prof
from django.shortcuts import render,get_object_or_404



def home(request):
	return render(request,'Area1/home.html',{'title':'Homepage'})


def about(request):
	return render(request,'Area1/about.html',{'title':'About Us'})


def prof_list(request):	
	context = {'pdata':Prof.objects.all()}
	return	render(request,'Area1/prof_list.html',context)


def prof_details(request,id):	
	prof = Prof.objects.get(id=id)

	context = {

	'data':prof
	}

	return render(request,'Area1/prof_details.html',context)