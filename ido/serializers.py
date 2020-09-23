from rest_framework import  serializers
from .models import Survey

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ('id','name','major','phone_num','body_temp','enter_time','agree_check','exit_time')