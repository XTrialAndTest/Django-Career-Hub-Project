from django.shortcuts import render, get_object_or_404
from .models import *


# Create your views here.
def job_detail(request, slug):
    job_detail = get_object_or_404(Job, slug=slug)
    return render(request, "job/job_detail.html", {"job": job_detail})
