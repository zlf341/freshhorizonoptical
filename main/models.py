from __future__ import unicode_literals

from django.db import models

# Create your models here.

class AppPermission():
    permit = models.CharField(max_length=50)
     
class AppDefinitions(models.Model):
    name = models.CharField(max_length=50)
    css = models.CharField(max_length=50)
    permit = models.ForeignKey(AppPermission, on_delete=models.CASCADE)

'''
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
'''
