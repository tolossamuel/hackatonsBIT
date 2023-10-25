from . import views
from django.urls import path


urlpatterns = [
	 path("", views.startHome, name = "startHome"),
	 path('login', views.login, name='login'),
     path('create', views.create, name='create'),
	 path('home/<str:pk>', views.home, name='home'),
	 path("save/<str:pk>",views.saveComments, name = "saveComments"),
	 path('search/<str:pk>', views.search, name = "search"),
	 path('addNew', views.createNew, name = "createNew"),
	 path('support', views.supportToCreate, name = "supportToCreate"),
	 path('profile/<str:pk>', views.profile, name = "profile"),
     path('search/', views.search_threads, name='search_threads'),
	 path("logout", views.logout, name = "logout"),
	 path("editProfile/<str:pk>", views.profileEdit, name= "profileEdit"),
]

