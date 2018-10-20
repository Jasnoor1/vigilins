from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from .models import UserDetail,ClientDetail,Fraud
from account.choices import INSURENCE_TYPE,USER_TYPE
from django.contrib.auth.models import User
import re
from django.core.exceptions import ObjectDoesNotExist

class FraudForm(forms.ModelForm):
    client_name = forms.ModelChoiceField(queryset=ClientDetail.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    # fraud_desc = forms.CharField(widget=TextInput(attrs={'class':'form-control text-box single-line'}))
    policy_id = forms.IntegerField(widget=TextInput(attrs={'class':'form-control text-box single-line'}))
    claim_no = forms.IntegerField(widget=TextInput(attrs={'class':'form-control text-box single-line'}))
    first_name = forms.CharField(widget=TextInput(attrs={'class':'form-control text-box single-line'}))
    pan_id = forms.CharField(widget=TextInput(attrs={'class':'form-control text-box single-line'}))
    aadhar_id = forms.IntegerField(widget=TextInput(attrs={'class':'form-control text-box single-line'}))
    # fraud_notified_date = forms.DateField()
    # fraud_status = forms.CharField(widget=TextInput(attrs={'class':'form-control text-box single-line'}))
    
    class Meta:
        model = Fraud
        fields =['client_name','policy_id','claim_no','first_name','pan_id','aadhar_id']

class CustomAuthForm(AuthenticationForm):
        username = forms.CharField(widget=TextInput(attrs={'class':'form-control','placeholder': 'Username'}))
        password = forms.CharField(widget=PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))


class UserForm(forms.ModelForm):
	insurence_company = forms.ModelChoiceField(queryset=ClientDetail.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
	first_name = forms.CharField(widget=TextInput(attrs={'class':'form-control text-box single-line'}))
	last_name = forms.CharField(widget=TextInput(attrs={'class':'form-control'}))
	middle_name = forms.CharField(widget=TextInput(attrs={'class':'form-control'}))
	email_id = forms.EmailField(widget=TextInput(attrs={'class':'form-control'}))
	user_name = forms.CharField(widget=TextInput(attrs={'class':'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
	account_validity = forms.CharField(widget=TextInput(attrs={'class':'form-control'}))
	user_type = forms.ChoiceField(choices=USER_TYPE,widget=forms.Select(attrs={'class':'form-control'}))
	class Meta:
		model = UserDetail
		fields = '__all__'
		fields = ['insurence_company','first_name','last_name','middle_name','email_id',\
        'user_name','password','account_validity','user_type']
        # fields = ['first_name','last_name','middle_name','email_id','user_name','password','account_validity']

class UserSearchForm(forms.ModelForm):
	insurence_company = forms.ChoiceField(choices=INSURENCE_TYPE,widget=forms.Select(attrs={'class':'form-control'}))
	first_name = forms.CharField(required=False,widget=TextInput(attrs={'class':'form-control text-box single-line'}))
	email_id = forms.EmailField(required=False,widget=TextInput(attrs={'class':'form-control text-box single-line'}))
	user_name = forms.CharField(required=False,widget=TextInput(attrs={'class':'form-control text-box single-line'}))
	class Meta:
		model = UserDetail
		# fields = '__all__'
		fields = ['insurence_company','first_name','email_id','user_name']


class SignUpForm(forms.ModelForm):
    username = forms.CharField(widget=TextInput(attrs={'class':'form-control','placeholder': 'Username'}))
    fullname = forms.CharField(widget=TextInput(attrs={'class':'form-control','placeholder': 'Fullname'}))
    email = forms.EmailField(widget=TextInput(attrs={'class':'form-control','placeholder': 'Email'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    # password1 = forms.CharField(required=False,widget=PasswordInput(attrs={'class':'form-control','placeholder':'Password1'}))
    # password2 = forms.CharField(widget=PasswordInput(attrs={'class':'form-control','placeholder':'Password2'}))


    class Meta:
        model = User
        fields = ['username','email','fullname','password']

    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     print("usernameeee",username)
    #     if not re.search(r'^\w+$', username):
    #         raise forms.ValidationError('Username can only contain alphanumeric characters and the underscore.')
    #     try:
    #     	print("inside try")
    #     	user = User.objects.get(username=username)
    #     	print("userrrr",user)
    #     except ObjectDoesNotExist:
    #     	print("inside except")
    #     	print("usernamamamam",username)
    #     	return username
    #     raise forms.ValidationError('Username is already taken.')