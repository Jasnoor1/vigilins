# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class SuperAdminFraud(models.Model):
    fraud_id = models.CharField(max_length=30,null = True,unique=True)
    policy_id = models.IntegerField(null = True)
    pan_id = models.CharField(max_length=30,null = True)
    aadhar_id = models.CharField(max_length=30,null = True)
    first_name = models.CharField(max_length=30,null = True)
    last_name = models.CharField(max_length=30,null =True)
    address = models.CharField(max_length=30,null = True)
    phone_no = models.CharField(max_length=30,null = True)
    fraud_desc = models.CharField(max_length=30,null = True)
    block_status = models.IntegerField(null = True)
    notification_status = models.IntegerField(null = True)
    fraud_date = models.DateField(null = True)
    fraud_identified_date = models.DateField(null = True)
    fraud_notified_date = models.DateField(null = True)
    fraud_reported_to_block = models.IntegerField(null = True)
    fraud_reported_to_block_date = models.DateField(null = True)
    fraud_type = models.CharField(max_length=30,null = True)
    fraud_status = models.CharField(max_length=30,null = True,blank=True)
    claim_no = models.CharField(max_length=30,null = True)
    vch_account_no = models.CharField(max_length=30,null = True)
    vch_beneficiary_name = models.CharField(max_length=30,null = True)
    vch_bank_name = models.CharField(max_length=30,null = True)
    vch_FS_code = models.CharField(max_length=30,null = True)
    vch_account_type = models.CharField(max_length=30,null = True)
    c_type = models.CharField(max_length=30,null = True)
    engine_number = models.CharField(max_length=30,null = True)
    chasis_no = models.CharField(max_length=30,null = True)
    registration_no = models.CharField(max_length=30,null = True)
    super_admin_flag = models.CharField(max_length=7, default='0')

    def __str__(self):
        return self.first_name

