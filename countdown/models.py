from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)


class Semester(models.Model):
    name = models.CharField(max_length=100)


class Day(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    date = models.DateField()
