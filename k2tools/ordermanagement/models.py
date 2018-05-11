# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Order(models.Model):
    order_nr = models.TextField(blank=True, null=True)
    customer = models.ForeignKey(Customer, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    deadline = models.TextField(blank=True, null=True)
    delivery_comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.order_nr


class Customer(models.Model):
    name = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    telegram = models.TextField(blank=True, null=True)
    referral = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class OrderItem (models.Model):
    unitload = models.TextField(blank=True, null=True)
    size = models.ForeignKey(Size)
    fabric1 = models.ForeignKey(Fabric, null=True)
    fabric2 = models.ForeignKey(Fabric, null=True)
    fabric3 = models.ForeignKey(Fabric, null=True)
    fabric4 = models.ForeignKey(Fabric, null=True)
    fabric5 = models.ForeignKey(Fabric, null=True)
    shape = models.ForeignKey(Shape)
    bootlace = models.ForeignKey(Bootlace, null=True)
    thread = models.ForeignKey(Thread, null=True)
    insole_sign = models.TextField(blank=True, null=True)
    glassing = models.BooleanField(default=False)
    shoe_tree = models.ForeignKey(ShoeTree, null=True)
    sole = models.ForeignKey(Sole)
    fat = models.ForeignKey(Fat, null=True)

    def __str__(self):
        return self.unitload


class ShoeTree(models.Model):
    title = models.TextField(blank=True, null=True)
    bootlace = models.ForeignKey(Bootlace, null=True)
    image = models.models.ImageField(upload_to='shoe_tree_images')

    def __str__(self):
        return self.title


class Sole(models.Model):
    title = models.TextField(blank=True, null=True)
    image = models.models.ImageField(upload_to='sole_images')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Thread(models.Model):
    title = models.TextField(blank=True, null=True)
    image = models.models.ImageField(upload_to='thread_images')
    description = models.TextField(blank=True, null=True)
    color = models.ForeignKey(Color)

    def __str__(self):
        return self.title


class Bootlace(models.Model):
    title = models.TextField(blank=True, null=True)
    image = models.models.ImageField(upload_to='bootlace_images')
    description = models.TextField(blank=True, null=True)
    color = models.ForeignKey(Color)

    def __str__(self):
        return self.title


class Size(models.Model):
    title = models.TextField(blank=True, null=True)
    sole = models.ForeignKey(Sole)

    def __str__(self):
        return self.title


class Shape(models.Model):
    title = models.TextField(blank=True, null=True)
    image = models.models.ImageField(upload_to='shape_images')

    def __str__(self):
        return self.title


class Sample (models.Model):
    sample = models.ForeignKey(OrderItem)
    image = models.models.ImageField(upload_to='sample_images')
