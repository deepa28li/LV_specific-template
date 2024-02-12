from django.db import models
from django.urls import reverse

# Create your models here.

class School(models.Model):
    sname=models.CharField(max_length=100)
    sprincipal=models.CharField(max_length=100)
    sloction=models.CharField(max_length=100)

    def gert_absolute_url(self):
        return reverse('school_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.sname

class Student(models.Model):
    stname=models.CharField(max_length=100)
    stage=models.IntegerField()
    sname=models.ForeignKey(School,on_delete=models.CASCADE,related_name='students')

