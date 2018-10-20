from django.conf.urls import url
from . import views

urlpatterns=[
    # url(r'$', views.home, name='home'),
    url(r'^uploads/form/$', views.model_form_upload, name='model_form_upload'),
    url(r'^uploads/simple/$', views.simple_upload, name='simple_upload'),
    url(r'^Upload/DownloadCSV/$',views.DownloadCSV),
]