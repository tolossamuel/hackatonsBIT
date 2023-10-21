from . import views
from django.urls import path


urlpatterns = [
	 path('', views.login, name='login'),
	 path('home/<str:pk>', views.home, name='home'),
]