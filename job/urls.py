from django.urls import path
from . import views

urlpatterns = [
    path("<slug:slug>", views.job_detail, name="job_detail"),
]
