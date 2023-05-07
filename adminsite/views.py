from typing import Any
from django.db import models
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .models import Course, Lesson, Enrollment
from django.urls import reverse
from django.views import generic, View
from django.http import Http404


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







