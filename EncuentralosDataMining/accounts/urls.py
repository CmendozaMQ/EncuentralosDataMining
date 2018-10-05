from django.conf.urls import url
# from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^signup/', views.signup, name='signup'),
    url(r'^login/', views.loginview, name='login'),
]