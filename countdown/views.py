from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404, render

from .models import *


def index(request, category_id=1):
    context = {}
    category = get_object_or_404(Category, pk=category_id)
    today = datetime.now().date()
    if category.name == "School":
        for s in Semester.objects.all():
            if s.start <= today and s.end >= today:
                semester = s
        total_days = Day.objects.filter(category_id=category_id, semester=semester, year=datetime.now().year).count()
        days_left = Day.objects.filter(category_id=category_id, semester=semester, year=datetime.now().year, date__gt=datetime.now()).count()
        context['title'] = "{} {}".format(semester, datetime.now().year)
    else:
        total_days = Day.objects.filter(category_id=category_id).count()
        days_left = Day.objects.filter(category_id=category_id, date__gt=datetime.now()).count()
        context['title'] = category.name

    context['category'] = category
    context['total_days'] = total_days
    context['days_left'] = days_left

    return render(request, 'countdown/countdown.html', context)
