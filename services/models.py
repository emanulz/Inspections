# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Service(models.Model):

    code = models.CharField(max_length=7, verbose_name='Código', unique=True, default=0)
    department = models.ForeignKey('ServiceDepartment', null=True, verbose_name='Familia', default='')
    subdepartment = models.ForeignKey('ServiceSubDepartment', null=True, verbose_name='Sub-Familia', default='')
    consecutive = models.DecimalField(default=0, max_digits=3, decimal_places=0, verbose_name='Consecutivo')
    description = models.CharField(max_length=255, verbose_name='Descripción del producto', default='')
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name='Precio ₡')
    unit = models.CharField(default='Unidad', max_length=255, verbose_name='Unidad')
    usetaxes = models.BooleanField(default=False, verbose_name='Usa Impuestos?')
    taxes = models.DecimalField(default=0, max_digits=5, decimal_places=2, verbose_name='Impuestos %')
    discount = models.DecimalField(default=0, max_digits=5, decimal_places=2, verbose_name='Descuento %')

    def __unicode__(self):
        return '%s' % self.product_description

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['code']


class ServiceDepartment(models.Model):

    name = models.CharField(max_length=255, verbose_name='Nombre de la Familia', unique=True)
    code = models.CharField(max_length=2, unique=True, verbose_name='Identificador de Familia')

    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']


class ServiceSubDepartment(models.Model):

    department = models.ForeignKey('ServiceDepartment', verbose_name='Familia')
    name = models.CharField(max_length=255, verbose_name='Nombre de la Sub-Familia', unique=True)
    code = models.CharField(max_length=2, verbose_name='Identificador de Sub-Familia')

    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Sub-Categoria'
        verbose_name_plural = 'Sub-Categorias'
        ordering = ['id']
