from django.conf.urls import url
from . import views

urlspatterns=[
    url('^$',views.welcome,name = 'Welcome'),
]