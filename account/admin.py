# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import UserDetail,ClientDetail,Fraud

# Register your models here.
admin.site.register(UserDetail)
admin.site.register(ClientDetail)
admin.site.register(Fraud)