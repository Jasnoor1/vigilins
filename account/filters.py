import django_filters

from account.models import UserDetail,Fraud

class UserFilter(django_filters.FilterSet):
	# insurence_company = django_filters.CharFilter(lookup_expr='icontains')
	# first_name = django_filters.CharFilter(lookup_expr='icontains')
	# user_name = django_filters.CharFilter(lookup_expr='icontains')
	# email_id = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = UserDetail
        fields = ['insurence_company', 'first_name', 'email_id','user_name' ]

class FraudFilter(django_filters.FilterSet):
	class Meta:
		model = Fraud
		fields = ['client_name','fraud_desc','policy_id','claim_no','first_name','pan_id','aadhar_id','fraud_notified_date','fraud_status']