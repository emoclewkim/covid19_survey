from django.db import models
#from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Survey(models.Model):
    name = models.CharField(max_length=20)               # 이름
    major = models.CharField(max_length=20)              # 전공  
    phone_num = models.CharField(default = '',max_length=13) 
    body_temp = models.DecimalField(max_digits=5,decimal_places=3)           #체온 - 입력(5자리숫자중 소수점아래 3자리표시)
    enter_time = models.DateTimeField()    # 입력시간
    agree_check = models.BooleanField()                     #동의여부
    exit_time = models.DateTimeField(blank=True, null=True) #퇴장시간날짜

    objects = models.Manager() # ~has no member vscode 에러 해결코드

    def __str__(self):
        return self.name

class graph_Survey(models.Model):
    exit_time = models.DateTimeField(blank=True, null=True) #퇴장시간날짜

    objects = models.Manager() # ~has no member vscode 에러 해결코드



