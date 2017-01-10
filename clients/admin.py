# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin
from .models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'id', 'address', 'email',)
    search_fields = ('id', 'name', 'phone', 'id', 'address', 'email',)
#   filter_horizontal = ('bill_product_list',)
