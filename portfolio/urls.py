from django.conf.urls import url
from django.urls import path
from . import views


app_name='portfolio'


urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^detail$', views.detail, name="detail"),
]


