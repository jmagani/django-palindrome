from django.conf.urls import url
from . import views

#URL pattern 
urlpatterns = [
    url(r'$', views.get_palindrome, name='palindrome'),
]
