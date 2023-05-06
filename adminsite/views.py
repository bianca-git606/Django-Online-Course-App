from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .models import Course, Lesson, Enrollment
from django.urls import reverse
from django.views import generic
from django.http import Http404


# Create your views here.

# display the top 10 popular courses
def popular_course_list(request):
    context = {}

    if request.method == 'GET':
        course_list = Course.objects.order_by('total_enrollment')[:10]
        context['course_list'] = course_list
        
        return render(request, 'onlinecourse/course_list.html', context)
    
def enroll(request, course_id):

    if request.method == 'POST':
        # searching the course, if not found print a 404 error 
        chosen_course = get_object_or_404(Course, pk=course_id)
        # and updating the total enrollment
        chosen_course.total_enrollment += 1
        chosen_course.save()
        # return an HTTP response redirecting user to course list view
        return HttpResponseRedirect(reverse(viewname='course_details', args=(chosen_course.id,)))
    

def course_details(request, course_id):
    
    context = {}
    if request.method == 'GET':
        try:
            course = Course.objects.get(pk=course_id)
            context['course'] = course
            
            return render(request, 'onlinecourse/course_details.html', context)
        
        except Course.DoesNotExist:
            return Http404("No course found with that course ID")


