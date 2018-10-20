# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import SuperAdminFraud
from adminuser.models import AdminFraud
from account.models import Fraud
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,FormView,DetailView
from datetime import datetime


# Create your views here.
class SuperAdminHomepage(TemplateView):
	def get(self,request):
		# objs = AdminFraud.objects.values('fraud_status').annotate(the_count=Count('fraud_status'))
		# counts_by_category = {f['fraud_status']: f['the_count'] for f in objs}
		# print("cdvgfu",counts_by_ca tegory)
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

		return render(request,"data/super_admin_dashboard.html")

class SuperAdminSuspiciousCase(TemplateView):
	# model = AdminFraud
	# template_name='data/admin_suspicious.html'
	def get(self,request):
		print('inside super admin get')
		obj = SuperAdminFraud.objects.all()
		return render(request,'data/super_admin_suspicious.html',{'object_list':obj})
	def post(self,request):
		print("inside post")
		value=request.POST.get('value')
		fraud_id=request.POST.get('fraud_id')
		print("value",value)
		print("fraud_id",fraud_id)
		print(".....")
		obj = AdminFraud.objects.filter(fraud_id=fraud_id).update(fraud_status=value,admin_flag='1',fraud_identified_date=datetime.now())
		obj1 = Fraud.objects.filter(fraud_id=fraud_id).update(fraud_status=value,fraud_identified_date=datetime.now())
		obj2 = SuperAdminFraud.objects.filter(fraud_id=fraud_id).update(fraud_status=value,super_admin_flag='1',fraud_identified_date=datetime.now())
		print("obj1 in post")
		# print("obj1,obj1",obj1)
		return redirect('super_admin_sus_cases')