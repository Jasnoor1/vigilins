# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,FormView
from django.shortcuts import render,redirect
from .models import UserDetail,Fraud,ClientDetail
from .forms import UserForm,UserSearchForm,SignUpForm,FraudForm
# from django.db.models import Q
from .filters import UserFilter,FraudFilter
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import auth
from adminuser.models import AdminFraud
from superadmin.models import SuperAdminFraud
import csv
import smtplib
from django.db.models import Count
from datetime import datetime

# from django.core.mail import send_mail
# Create your views here.

class Homepage(TemplateView):
	def get(self,request):
		objs = Fraud.objects.values('fraud_status').annotate(the_count=Count('fraud_status'))
		counts_by_category = {f['fraud_status']: f['the_count'] for f in objs}
		print("category of moderator",counts_by_category)
		return render(request,"data/dashboard.html",{'data':counts_by_category})

# class UpdateFraudCase(UpdateView):
# 	model = Fraud
# 	form_class = UpdateFraudForm
# 	success_url = '/suspicious_cases/'
# 	template_name='data/update_fraud_case.html'


# def suspiciousCases(request):
# 	with open('/home/mahimachaudhary/import.csv') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         # The header row values become your keys
#         suite_name = row['SuiteName']
#         test_case = row['Test Case']
#         # etc....

#         new_revo = Revo(SuiteName=suite_name, TestCase=test_case,...)
#         new_revo.save()


class SuspiciousCases(TemplateView):
	model = Fraud
	
	
	template_name='data/suspicious.html'
	
	def get(self,request):
		obj = Fraud.objects.all()
		print("inside suspicious_cases")
		# remark=request.session['remarks']
		# print("remark",remark)
		return render(request,'data/suspicious.html',{'object_list':obj})
	def post(self,request):
		print("inside post of suspicious case")
		pk=request.POST.get('id')
		remark=request.POST.get('remark')
		objs = Fraud.objects.filter(pk=pk)
		string='fraud'
		count = pk
		for obj in objs:
			string = string + pk
			obj.fraud_id = string
			obj.flag = '1'
			self.request.session['fraud_id']=obj.fraud_id
			obj.fraud_status = 'Case_Inspecting'
			obj.fraud_notified_date = datetime.now()
			obj.save()
			admin_obj = AdminFraud.objects.create(fraud_id=string,fraud_desc=obj.fraud_desc,policy_id=obj.policy_id,claim_no=obj.claim_no,first_name=obj.first_name,pan_id=obj.pan_id,aadhar_id=obj.aadhar_id,fraud_status=obj.fraud_status,fraud_notified_date=obj.fraud_notified_date)
			admin_obj.save()
			print("dmin obj",admin_obj)
			super_admin_obj = SuperAdminFraud.objects.create(fraud_id=string,fraud_desc=obj.fraud_desc,policy_id=obj.policy_id,claim_no=obj.claim_no,first_name=obj.first_name,pan_id=obj.pan_id,aadhar_id=obj.aadhar_id,fraud_status=obj.fraud_status,fraud_notified_date=obj.fraud_notified_date)
			super_admin_obj.save()
			print("super_admin",obj)
		request.session['remarks']=remark
		return redirect('sus_case')


class CreateUpdate(TemplateView):
   template_name = 'data/create_update.html'

class Token(ListView):
	model = ClientDetail
	template_name='data/token.html'

class DataUpload(TemplateView):
	template_name='data/data_upload.html'
	
class VigilinsRating(TemplateView):
	template_name='data/vigilins_rating.html'

class Base(TemplateView):
	template_name='data/base.html'

class AddUser(CreateView):
	def get(self,request):
		user_form = UserForm()
		return render(request,'data/add_user.html',{'form':user_form})
	
	def post(self,request):
		form = UserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('user')
		form = UserForm()
		return render(request,'data/add_user.html',{'form':form})

class User(ListView):
	model = UserDetail
	template_name='data/user.html'
	
	def get_context_data(self,**kwargs):
		context = super(User,self).get_context_data(**kwargs)
		context['filter'] = UserFilter(self.request.GET,queryset=self.get_queryset())
		print("context",context)
		return context

class UpdateRecord(UpdateView):
	model = UserDetail
	form_class = UserForm
	success_url = '/user/'
	template_name='data/add_user.html'

class AddSuspiciousCases(CreateView):
	
	def get(self,request):
		print("inside get")
		user_form = FraudForm()
		return render(request,'data/suspicious_cases.html',{'form':user_form})
	
	def post(self,request):
		print("inside post")
		form = FraudForm(request.POST)
		print("form",form)
		print("error",form.errors)
		if form.is_valid():
			print("inside valid")
			form.save()
			print("yes i m saved")
			return redirect('user')
		form = FraudForm()
		return render(request,'data/suspicious_cases.html',{'form':form})

class Notify(TemplateView):
	template_name='data/notify.html'

class ConfirmedFraud(TemplateView):
	template_name='data/confirmed_fraud.html'

class CleanCases(TemplateView):
	template_name='data/clean_case.html'

class WriteToBlock(TemplateView):
	template_name='data/write_to_block.html'



class SignUp(CreateView):
    # form_class = SignUpForm
    # success_url = '/login/'
    # template_name = 'data/pages-register.html'

    def get(self,request):
        user_form = SignUpForm()
        return render(request,'data/pages-register.html',{'form':user_form})


    def post(self,request):
        form = SignUpForm(request.POST)
        if form.is_valid():
    		print("inside valid")
    		user = form.save(commit=False)
    		username = form.cleaned_data['username']
    		raw_password = user.set_password(form.cleaned_data['password'])
    		email = form.cleaned_data['email']
    		print(username,raw_password,email)
    		user.save()
    		user = auth.authenticate(username=username, password=raw_password, email=email)
    		print("user",user)
    		login(request, user)
    		# user.save()
    		return redirect('login')
        else:
            form = SignUpForm()
        return render(request,'data/pages-register.html',{'form':form})


class Notify(UpdateView):

    def get(self,request,pk):
        remark = request.session['remarks']
        print("remarkkkk",remark)
        return render(request,'data/notifies.html')

    def post(self,request,pk):
        objs = Fraud.objects.filter(pk=pk)
        string='fraud'
        count = pk
        for obj in objs:
                string = string + pk
                obj.fraud_id = string
                self.request.session['fraud_id']=obj.fraud_id
                obj.fraud_status = 'Case_Inspecting'
                obj.fraud_notified_date = datetime.now()
                obj.save()
                admin_obj = AdminFraud.objects.create(fraud_id=string,fraud_desc=obj.fraud_desc,policy_id=obj.policy_id,claim_no=obj.claim_no,first_name=obj.first_name,pan_id=obj.pan_id,aadhar_id=obj.aadhar_id,fraud_status=obj.fraud_status,fraud_notified_date=obj.fraud_notified_date)
                admin_obj.save()
                print("admin obj",admin_obj)
        request.session['remarks']=request.POST.get('remark')
        return redirect('sus_case')


def send_mail():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.login("s9412856492@gmail.com", "*G33k001")
	msg = "hello"
	server.sendmail("s9412856492@gmail.com", "mahimabajwa62@gmail.com", msg)