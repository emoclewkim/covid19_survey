from rest_framework import  serializers
from .models import Survey, graph_Survey

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ('id','name','major','phone_num','body_temp','enter_time','agree_check','exit_time')

class graph_SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = graph_Survey
        fields = ('name', 'exit_time')