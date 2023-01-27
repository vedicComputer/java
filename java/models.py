from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Topic(models.Model):
    topicid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=18,default="")
    def __str__(self):
        return self.name
class Quiz(models.Model):
    quizid = models.AutoField(primary_key=True)
    question = models.CharField(max_length=150,default="")
    optionA = models.CharField(max_length=28,default="")
    optionB = models.CharField(max_length=28,default="")
    optionC = models.CharField(max_length=28,default="")
    optionD = models.CharField(max_length=28,default="")
    answer = models.CharField(max_length=28,default="")
    topic = models.ManyToManyField(Topic,blank=True)
    def __str__(self):
        return self.question
