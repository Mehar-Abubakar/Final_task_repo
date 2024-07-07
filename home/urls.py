from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "Login to Meher Abubakar"
admin.site.site_title = "Welcome to Dashboard"
admin.site.index_title = "Welcome to Portal"

urlpatterns = [
    path('', views.home, name='home'),
    path('project/', views.project, name='project'),
    path('contact/', views.contact, name='contact'),
]
