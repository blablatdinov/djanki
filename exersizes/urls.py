from django.urls import path

from exersizes.views import hello_view

urlpatterns = [
	path('hello', hello_view),
]