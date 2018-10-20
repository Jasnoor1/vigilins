from django.conf.urls import url
from .views import *
from django.contrib.auth import views as auth_views
from .forms import CustomAuthForm

urlpatterns = [
            url(r'^dashboard/$', Homepage.as_view(),name='home'),
            url(r'^suspicious_cases/$', SuspiciousCases.as_view(),name='sus_case'),
            url(r'^user/$', User.as_view(),name='user'),
            url(r'^token/$', Token.as_view(),name='token'),
            url(r'^noify/$', Notify.as_view(),name='notify'),
            url(r'^wite_to_block/$', WriteToBlock.as_view(),name='write'),
            url(r'^confirmed_fraud/$', ConfirmedFraud.as_view(),name='confirmed_fraud'),
            url(r'^clean_cases/$', CleanCases.as_view(),name='clean_cases'),
            url(r'^add_user/$', AddUser.as_view(),name='add_user'),
            url(r'^data_upload/$', DataUpload.as_view(),name='data_upload'),
            # url(r'^data_upload/$', DataUpload.as_view(),name='data_upload'),
            url(r'^add_suspicious_cases/$', AddSuspiciousCases.as_view(),name='add_sus_case'),
            url(r'^update_data/(?P<pk>\w+)$', UpdateRecord.as_view(),name='update_data'),
            url(r'^vigilins_rating/$', VigilinsRating.as_view(),name='vig_rating'),
            url(r'^base/$', Base.as_view(),name='base'),
            url(r'^login/$', auth_views.login, name='login', kwargs={"authentication_form":CustomAuthForm}),
            url(r'^logout/$', auth_views.logout, name='logout'),
            # url(r'^createUpd/$',CreateUpdate.as_view(),name='createupdate'),)
            url(r'^signup/$', SignUp.as_view(), name='signup'),
            url(r'^notify/(?P<pk>\w+)$',Notify.as_view(),name='notify')


            ]

