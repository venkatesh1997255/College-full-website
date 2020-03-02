# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Application, StudentRegistration, User, StaffRegistration
from .student_registrationform import RegistrationForm, UserForm
from .applicationform import ApplicationForm
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .staff_registartion import StaffRegistrationForm, StaffUserForm


def index(request):
    return render(request, 'College/index.html', )


def application(request):
    # import pdb;pdb.set_trace()
    if request.method == 'POST':
        Application.objects.create(
            name=request.POST['name'],
            gender=request.POST['gender'],
            email=request.POST['email'],
            dob=request.POST['dob'],
            department=request.POST['department'],
            ssc_marklist=request.FILES['ssc_marklist'],
            inter_marklist=request.FILES['inter_marklist'],

        )
        return HttpResponseRedirect(reverse('College:index'))
    return render(request, 'College/ApplicationForm.html', {})


def student_registration(request):
    if request.method == 'GET':
        form1 = UserForm()
        form2 = RegistrationForm()
        return render(request, 'College/RegistrationForm.html', {'form1': form1, 'form2': form2})
    form1 = UserForm(request.POST)
    form2 = RegistrationForm(request.POST, request.FILES)
    email = request.POST['email']
    studenta = Application.objects.filter(email=email, is_verified=True)
    studentb = Application.objects.get(email=email, is_verified=True)

    if studenta.exists() and form2.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = User.objects.create_user(username, email, password)

        StudentRegistration.objects.create(
            user=user,
            name=studentb,
            age=form2.data["age"],
            father_name=form2.data["father_name"],
            mother_name=form2.data["mother_name"],
            profile_pic=request.FILES.get("profile_pic")
        )
        return HttpResponseRedirect(reverse('College:index'))

    return render(request,
                  'College/RegistrationForm.html',
                  {'form1': form1, 'form2': form2})


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'College/student_profile.html', {})

        else:
            return HttpResponse("user not found")

    else:
        return render(request, 'College/user_login.html', {})


def student_profile(request):
    student = StudentRegistration.objects.get(user__username=request.user)
    return render(request, 'College/student_profile.html', {'student': student})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('College:index'))


def staff_registration(request):
    if request.method == "POST":
        form1 = StaffUserForm(request.POST)
        form2 = StaffRegistrationForm(request.POST, request.FILES)
        # import ipdb
        # ipdb.set_trace()

        if form1.is_valid() and form2.is_valid():
            # import ipdb
            # ipdb.set_trace()
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
            user = User.objects.create_user(username, email, password)
            StaffRegistration.objects.create(

                name=form2.data['name'],
                user=user,
                father_name=form2.data['father_name'],
                mother_name=form2.data['mother_name'],
                profile_pic=request.FILES.get("profile_pic"),
                department=form2.data['department'],
                age=form2.data['age'],
                salary=form2.data['salary'],
                gender=form2.data['gender'],
            )
            HttpResponse('success')
            # return HttpResponseRedirect(reverse('College:index'))
        else:
            HttpResponse('failed')

    else:
        form1 = StaffUserForm()
        form2 = StaffRegistrationForm()
        return render(request, 'College/staffregistration.html', {'form1': form1, 'form2': form2})
