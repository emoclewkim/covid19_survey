from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Survey, graph_Survey
from django.utils import timezone
from rest_framework import viewsets
from .serializers import SurveySerializer, graph_SurveySerializer

# Create your views here.

def home(request):
    return render(request, 'home.html')

def new(request):
    return render(request, 'new.html')

def create(request):
    survey = Survey()

    survey.name = request.GET['name']
    survey.major = request.GET['major']
    survey.phone_num = request.GET['phone_num']
    survey.body_temp = request.GET['body_temp']
    survey.agree_check = request.GET['chk_info']
    survey.enter_time = timezone.datetime.now()
    survey.exit_time = None

    survey.save()
    return HttpResponseRedirect(reverse('new'))

class SurveyViewset(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

class graph_SurveyViewset(viewsets.ModelViewSet):
    queryset = graph_Survey.objects.all()
    serializer_class = graph_SurveySerializer

def exit(request):
    return render(request, 'exit.html')
