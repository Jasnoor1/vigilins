from __future__ import unicode_literals

from django.db import models




# Create your models here.

class Document(models.Model):
    description = models.CharField(max_length=255, blank= True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)



class Suspicious_Cases(models.Model):
    Claim_No = models.IntegerField(primary_key=True,max_length=60)
    Emp_Name = models.CharField(max_length= 30)
    Card_No = models.IntegerField(max_length=15)
    Policy_no = models.CharField(max_length= 37)
    Policy_from = models.DateTimeField()
    Sum_Insured = models.IntegerField(max_length=50)
    Group_Name = models.CharField(max_length=60)
    NSP_City = models.CharField(max_length=45)

class CreateCSVList(models.Model):
    ColumnName = models.CharField(max_length=50)
