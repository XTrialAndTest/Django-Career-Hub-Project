from django.urls import path
from . import views

urlpatterns = [
    path("search", views.search, name="search"),
    path('job_applications', views.job_application, name="job_application"),
    path('job_creation', views.job_creation, name="job_creation"),
    path('job_applied', views.job_applied, name="job_applied"),
    path("<slug:slug>", views.job_category_detail, name="job_category_detail"),
    path("<slug:job_category_slug>/<slug:slug>",
         views.job_detail, name="job_detail"),

]
