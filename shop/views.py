from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import  Category, Course

def index(request): 
    courses = Course.objects.all()
    return render(request, "shop/courses.html", {"courses": courses})


def single_course(request, course_id):
    try:
        course = Course.objects.get(pk=course_id)
        return render(request, "shop/single_course.html", {"course": course})
    except Course.DoesNotExist:
        raise Http404()