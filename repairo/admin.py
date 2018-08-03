# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Repair, Car

admin.site.register(Repair)
admin.site.register(Car)
