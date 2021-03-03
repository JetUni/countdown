from django.db import models
from datetime import datetime, timedelta


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Semester(models.Model):
    name = models.CharField(max_length=100)
    start = models.DateField(default=None)
    end = models.DateField(default=None)

    def __str__(self):
        return self.name


class Day(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    date = models.DateField()

    def __str__(self):
        if self.category.name == "School":
            return "{} {} - {}".format(self.semester, self.year, self.date.strftime("%Y-%m-%d"))
        else:
            return self.date.strftime("%Y-%m-%d")
