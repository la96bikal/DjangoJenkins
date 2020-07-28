from django.urls import path
from . import views
#just a comment
#just another comment and another one
urlpatterns = [
	path('', views.hello, name = 'hello'),
	path('<int:id>', views.hello)
]