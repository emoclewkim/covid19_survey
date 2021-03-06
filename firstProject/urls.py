"""firstProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
import ido.views
from ido import views
from rest_framework import routers
from django.conf.urls import url, include
from ido.views import graph_SurveyViewset

router = routers.DefaultRouter()
router.register(r'surveys',views.SurveyViewset)
router.register('graph_Surveys',graph_SurveyViewset)

urlpatterns = [
    path('admin/', admin.site.urls,),
    path('',ido.views.home, name='home'),
    path('new/',ido.views.new, name='new'),
    path('new2/',ido.views.new2, name='new2'),
    path('create/', ido.views.create, name='create'),
    path('create2/', ido.views.create2, name='create2'),
    url(r'^',include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('exit/',ido.views.exit, name='exit'),
]
