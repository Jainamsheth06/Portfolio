from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/submit/', views.contact_submit, name='contact_submit'),
    path('api/projects/<slug:slug>/', views.project_detail_api, name='project_detail_api'),
]
