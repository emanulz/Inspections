# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin
from .models import Service, ServiceDepartment, ServiceSubDepartment


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'department', 'subdepartment',
                    'price', 'unit', 'discount', 'usetaxes', 'taxes')

    search_fields = ('id', 'code', 'description', 'department__name',
                     'subdepartment__name', 'price', 'unit',
                     'usetaxes', 'taxes')
#   filter_horizontal = ('bill_product_list',)


@admin.register(ServiceDepartment)
class ServiceDepartmentAdmin(admin.ModelAdmin):
    list_display = ('code', 'name',)
    search_fields = ('code', 'name',)


@admin.register(ServiceSubDepartment)
class ServiceSubDepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'code', )
    search_fields = ('code', 'name',
                     'department__name',)
