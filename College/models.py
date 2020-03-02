# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


department_choice = [
    ('mech', 'mechanical engineering'),
    ('cse', 'computers science engineering'),
    ('eee', 'electrical engineering'),
    ('ece', 'electronic engineering'),
]
gender_choice = [
    ('M', 'male'),
    ('F', 'female'),
    ('O', 'others'),
]


# class TimeStampedModel():
#
#
#     class Meta:
#         abstract = True


class Application(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=5, choices=gender_choice)
    department = models.CharField(max_length=5, choices=department_choice)
    ssc_marklist = models.FileField(upload_to='document/')
    inter_marklist = models.FileField(upload_to='document/')
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return '{},{},{}'.format(self.name, self.email, self.is_verified)


class StudentRegistration(models.Model):
    name = models.OneToOneField(
        Application,
        on_delete=models.CASCADE)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='image/')
    age = models.IntegerField(default=0)

    def __str__(self):
        return "{} {}".format(self.name, self.user.username)


class StaffRegistration(models.Model):
    name = models.CharField(max_length=50)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='image/')
    department = models.CharField(max_length=5, choices=department_choice)
    age = models.IntegerField(default=0)
    salary = models.IntegerField(default=0)
    gender = models.CharField(max_length=5, choices=gender_choice)

    def __str__(self):
        return "{} {}".format(self.name, self.user.username)
