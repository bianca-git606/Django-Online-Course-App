from typing import Any
from django.db import models
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .models import Course, Lesson, Enrollment
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.views import generic, View
from django.http import Http404
from django.contrib.auth.models import User
import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)


# display the top 10 popular courses

class CourseListView(generic.ListView):

    template_name = 'onlinecourse/course_list.html'
    context_object_name = 'course_list'

    def get_queryset(self):
        course_list = Course.objects.order_by('total_enrollment')[:10]
        return course_list



class EnrollView(View):
    
    def post(self, request, *args, **kwargs):
        
        course_id = kwargs.get('course_id')
        # searching the course, if not found print a 404 error 
        chosen_course = get_object_or_404(Course, pk=course_id)
        # and updating the total enrollment
        chosen_course.total_enrollment += 1
        chosen_course.save()
        # return an HTTP response redirecting user to course list view
        return HttpResponseRedirect(reverse(viewname='course_details', args=(chosen_course.id,)))


class CourseDetailsView(View):

    def get(self, request, *args, **kwargs):

        context = {}
        # get the param
        course_id = kwargs.get("course_id")
        # returns a 404 error if not exists
        course = get_object_or_404(Course, pk=course_id)
        context["course"] = course
        return render(request, 'onlinecourse/course_details.html', context)
    
def logout_request(request):

    # get the user object based on session id in request
    print(f"User {request.user.username} is logging out.")
    # logout user in the request
    logout(request)
    # redirect user back to course list view
    return redirect('popular_course_list')

def login_request(request):
    context = {}
    # handles POST request
    if request.method == "POST":
        # Get username and password from request.POST dictionary
        username = request.POST['username']
        password = request.POST['psw']
        # Try to check if provide credential can be authenticated
        user = authenticate(username=username, password=password)
        if user is not None:
            # If user is valid, call login method to login current user
            login(request, user)
            return redirect('popular_course_list')
        else:
            # If not, return to login page again
            return render(request, 'onlinecourse/user_login.html', context)
    else:
        return render(request, 'onlinecourse/user_login.html', context)

def registration_request(request):
    context = {}
    # If it is a GET request, just render the registration page
    if request.method == 'GET':
        return render(request, 'onlinecourse/user_registration.html', context)
    # If it is a POST request
    elif request.method == 'POST':
        # Get user information from request.POST
        username = request.POST['username']
        password = request.POST['psw']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_exist = False
        try:
            # Check if user already exists
            User.objects.get(username=username)
            user_exist = True
        except:
            # If not, simply log this is a new user
            logger.debug("{} is new user".format(username))
        # If it is a new user
        if not user_exist:
            # Create user in auth_user table
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                            password=password)
            # Login the user and redirect to course list page
            login(request, user)
            return redirect("popular_course_list")
        else:
            return render(request, 'onlinecourse/user_registration.html', context)






