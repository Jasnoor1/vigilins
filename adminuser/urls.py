from django.conf.urls import url
from .views import *

urlpatterns = [
            url(r'^admin_dashboard/$', AdminHomepage.as_view(),name='admin_home'),
            url(r'^admin_suspicious_cases/$', AdminSuspiciousCase.as_view(),name='admin_sus_cases'),
            url(r'^clean_cases/', CleanFraud.as_view(),name='clean'),
            # (?# url(r'^admin_dashboard/$', AdminHomepage.as_view(),name='admin_home'))
            ]