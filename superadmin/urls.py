from django.conf.urls import url
from .views import *

urlpatterns = [
            url(r'^super_admin_dashboard/$', SuperAdminHomepage.as_view(),name='super_admin_home'),
            url(r'^super_admin_suspicious_cases/$', SuperAdminSuspiciousCase.as_view(),name='super_admin_sus_cases'),
            # url(r'^clean_cases/', CleanFraud.as_view(),name='clean'),
            # (?# url(r'^admin_dashboard/$', AdminHomepage.as_view(),name='admin_home'))
            ]