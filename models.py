from django.db import models


class Registration(models.Model):
    name=models.CharField(max_length=200)
    contact=models.IntegerField(null=True)
    email=models.EmailField(null=True)
    password=models.CharField(max_length=200)
    kaggle_result=models.IntegerField(null=True)
    flutter_result=models.IntegerField(null=True)
    kotlin_result=models.IntegerField(null=True)
    android_development_result=models.IntegerField(null=True)
    firebase_result=models.IntegerField(null=True)
    gemini_result=models.IntegerField(null=True)


class kaggle_questions(models.Model):
    question = models.TextField() 
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    answer=models.CharField(max_length=100)

class android_development_questions(models.Model):
    question = models.TextField() 
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    answer=models.CharField(max_length=100)

class flutter_questions(models.Model):
    question = models.TextField() 
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    answer=models.CharField(max_length=100)

class kotlin_questions(models.Model):
    question = models.TextField() 
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    answer=models.CharField(max_length=100)

class firebase_questions(models.Model):
    question = models.TextField() 
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    answer=models.CharField(max_length=100)

class gemini_questions(models.Model):
    question = models.TextField() 
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    answer=models.CharField(max_length=100)