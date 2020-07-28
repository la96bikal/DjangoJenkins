from django.urls import path
from . import views
#just a comment
urlpatterns = [
	path('', views.hello, name = 'hello'),
	path('<int:id>', views.hello)
]