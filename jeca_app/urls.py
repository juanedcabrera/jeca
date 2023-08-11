"""
URL configuration for jeca_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from jeca_backend import views
from rest_framework import routers

# router
router = routers.DefaultRouter()
router.register(r'jobs', views.JobViewSet)



urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    # path('jobs/', views.job_list),
    path('companies/', views.company_list),
    path('resumes/', views.resume_list),
    path('coverletters/', views.cover_letter_list)
]
