from django.conf.urls import include, url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^scrapeDataBlank/', views.scrapeDataBlank, name='scrapeDataBlank'),
    url(r'^scrapeData_page/', views.scrapeData_page, name='scrapeData_page'),
    url(r'^scrapeData/', views.scrapeData, name='scrapeData'),
    url(r'^about/', views.about, name='about'),
    url(r'^home_setup/', views.home_setup, name='home_setup'),
    url(r'^save_post/', views.save_post, name='save_post'),
    url(r'^save_post_data/', views.save_post_data, name='save_post_data'),
    url(r'^savePost_page/', views.savePost_page, name='savePost_page'),
    url(r'^export/csv/$', views.export_post_csv, name='export_post_csv'),
]
