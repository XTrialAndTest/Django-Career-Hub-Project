from django.shortcuts import render, get_object_or_404
from .models import *


# Create your views here.
def job_detail(request, job_category_slug, slug):
    job_detail = get_object_or_404(Job, slug=slug)
    return render(request, "job/job_detail.html", {"job": job_detail})


def job_category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    job = category.jobs.all()
    return render(request, "job/job_category_detail.html", {"category": category, 'job': job})
