# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView,CreateView,ListView,UpdateView,FormView,DetailView
from django.shortcuts import render,redirect
from account.models import Fraud 
from adminuser.models import AdminFraud
from django.http import HttpResponse
from django.db.models import Count
from datetime import datetime

# from .forms import UserForm,UserSearchForm,SignUpForm,FraudForm
# from django.db.models import Q
# from .filters import UserFilter,FraudFilter
# Create your views here.
class AdminHomepage(TemplateView):
	def get(self,request):
		objs = AdminFraud.objects.values('fraud_status').annotate(the_count=Count('fraud_status'))
		counts_by_category = {f['fraud_status']: f['the_count'] for f in objs}
		print("cdvgfu",counts_by_category)
		# adminList = []
		# for obj in objs:
		# 	print("obj",obj)
			# print("ejfbvge",obj.fraud_status)
		# 	adminDict = {}
		# 	if obj.fraud_status == 'clean':
		# 		adminDict["clean"] = obj.the_count
		# 		adminList.append(adminDict)
		# 	if obj.fraud_status == 'fraud':
		# 		adminDict["fraud"] = obj.the_count
		# 		adminList.append(adminDict)
		# 	if obj.fraud_status == 'Case Inspecting':
		# 		adminDict["inspecting"] == obj.the_count
		# 		adminList.append(adminDict)
		# print("listtt",adminList)


		# for i in obj:
			# print("gdef",i.count())

		return render(request,"data/admin_dashboard.html",{'data':counts_by_category})

class AdminSuspiciousCase(TemplateView):
	# model = AdminFraud
	# template_name='data/admin_suspicious.html'
	def get(self,request):
		# print("ffffffffffiiiiiiiiiiii",self.request.session['fraud_id'])
		obj = AdminFraud.objects.all()
		print("inside get in get function")
		# adminList=[]
		# for i in obj:
		# 	admindict=dict()
		# 	admindict["fraud_id"]=i.fraud_id
		# 	admindict["first_name"]=i.first_name
		# 	adminList.append(admindict)
		# print("list",adminList)
		# print("obj",obj)
		return render(request,'data/admin_suspicious.html',{'object_list':obj})
	def post(self,request):

		print("inside post")
		value=request.POST.get('value')
		fraud_id=request.POST.get('fraud_id')
		print("value",value)
		print("fraud_id",fraud_id)
		print(".....")
		# l=updateadmin(request)
		# print("llll",l)
		obj = AdminFraud.objects.filter(fraud_id=fraud_id).update(fraud_status=value,fraud_identified_date=datetime.now())
		# print("obj in post")
		print("obj,obj",obj)
		obj1 = Fraud.objects.filter(fraud_id=fraud_id).update(fraud_status=value,fraud_identified_date=datetime.now())
		print("obj1 in post")
		print("obj1,obj1",obj1)
		return redirect('admin_sus_cases')

# def udateadmin(request):
# 	obj = AdminFraud.objects.filter(fraud_id=fraud_id).update(fraud_status=value)
# 	print("obj in post")
# 	print("obj,obj",obj)
# 	obj1 = Fraud.objects.filter(fraud_id=fraud_id).update(fraud_status=value)
# 	print("obj1 in post")
# 	print("obj1,obj1",obj1)
# 	return obj1,obj2	


def updatequery(request):
	obj = AdminFraud.objects.filter(fraud_id=fraud_id).update(fraud_status=value)
	obj1 = Fraud.objects.filter(fraud_id=fraud_id).update(fraud_status=value)
	return obj,obj1

class CleanFraud(DetailView):
	model=AdminFraud
	def post(self,request,pk):
		print("inide post")
		clean=self.request.POST.get('clean')
		print("clean",clean)
		return render(request,'data/admin_suspicious.html')