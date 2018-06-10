from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$|time_display/$', views.index),
]