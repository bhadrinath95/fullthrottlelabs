from django.db import models

# Create your models here.
class Activity_Period(models.Model):
    start_time = models.DateTimeField(auto_now_add=False)
    end_time = models.DateTimeField(auto_now_add=False)
    
class Member(models.Model):
    member_id = models.CharField(max_length=50)
    real_name = models.CharField(max_length=100)
    tz = models.CharField(max_length=100)
    activity_periods = models.ManyToManyField(Activity_Period)
    def __str__(self):
        return self.member_id
    
class Membership(models.Model):
    ok = models.BooleanField(default=False)
    members = models.ManyToManyField(Member)