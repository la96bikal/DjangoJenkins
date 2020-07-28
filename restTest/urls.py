from django.urls import path
from . import views
#just a comment
#just another comment
urlpatterns = [
	path('', views.hello, name = 'hello'),
	path('<int:id>', views.hello)
]