from django.urls import path
from . import views
from .api import *



urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('post-a-job/', views.post_a_job, name='post_a_job'),
    path('contact-us', views.contact, name='contact'),
    path('<slug:category_slug>', views.job_list, name='job_list_category'),
    path('<slug:job_slug>/', views.job_detail, name='job_detail'),

    ### API
    path('api/jobs/', JobListView.as_view(), name='api-list-view'),
    path('api/jobs/<int:id>/', JobDetailView.as_view(), name='api-detail-view'),
]