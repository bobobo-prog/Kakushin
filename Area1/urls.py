from django.urls import path
from . import views


urlpatterns = [
	path('',views.home,name='Area1-home'),
	path('about/',views.about,name='Area1-about'),
	path('prof_list/',views.prof_list,name='Area1-prof-list'),
	path('prof_list/prof_details/<int:id>/',views.prof_details,name='Area1-prof-details')
]