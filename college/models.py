from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Student(models.Model):
    student_id = models.IntegerField()
    name = models.CharField(max_length=55)
    start_year = models.IntegerField()


class Professor(models.Model):
    professor_id = models.IntegerField()
    name = models.CharField(max_length=55)
    office_number = models.IntegerField()
    salary = models.FloatField()

    def __unicode__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=55)
    department = models.CharField(max_length=55)
    number = models.IntegerField()

    def __unicode__(self):
        return self.name


class Section(models.Model):
    name = models.CharField(max_length=55)
    course = models.ForeignKey(Course)
    professor = models.ForeignKey(Professor)