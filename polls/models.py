from __future__ import unicode_literals

from django.db import models


class Teacher(models.Model):
	firstName = models.CharField(max_length=30)
	lastName = models.CharField(max_length=30)
	officeDetails = models.CharField(max_length=30)
	phone = models.CharField(max_length=30)
	email = models.EmailField(max_length=50)



class Student(models.Model):
	firstName = models.CharField(max_length=30)
	lastName = models.CharField(max_length=30)
	email = models.EmailField(max_length=50)
	courses = models.ManyToManyField(Course)


class Course(models.Model):
	name = models.CharField(max_length=30)
	code = models.CharField(max_length=30)
	classroom = models.CharField(max_length=30)
	times = models.CharField(max_length=50)
	teacher = models.ForeignKey(Teacher)