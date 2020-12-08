from datetime import date

from django.db import models


class ContactModel(models.Model):
    name=models.CharField(max_length=32)
    email=models.EmailField(max_length=32)
    phone=models.IntegerField()
    courses = models.CharField(max_length=32)
    shifts=models.CharField(max_length=32)
    location = models.CharField(max_length=32)
    gender = models.CharField(max_length=6)
    start_date=models.DateField()

class AdminLoginModel(models.Model):
    User_Name=models.CharField(max_length=32)
    Password=models.CharField(max_length=20)
class AddCourseModel(models.Model):
    course_id=models.IntegerField()
    course_name=models.CharField(max_length=32)
    course_duration=models.IntegerField()
    course_fee=models.IntegerField()
    course_start_date=models.DateField()
    course_start_time=models.TimeField()
    course_trainer_name=models.CharField(max_length=32)
    course_trainer_exp=models.FloatField()
class FeedBackModel(models.Model):
    name=models.CharField(max_length=32)
    rating=models.IntegerField()
    feedback=models.CharField(max_length=200)
    feedback_date = models.DateField()

