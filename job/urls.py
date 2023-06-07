from django.urls import path
from . import views

urlpatterns = [
    path("<slug:slug>", views.job_category_detail, name="job_category_detail"),
    path("<slug:job_category_slug>/<slug:slug>",
         views.job_detail, name="job_detail"),
]
