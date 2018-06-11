from datetime import datetime, timedelta
from django.shortcuts import render

from .models import *


def index(request):
    context = {}
    context['total_days'] = Day.objects.filter(category_id=1, year=datetime.now().year).count()
    context['days_left'] = Day.objects.filter(category_id=1, date__gt=datetime.now()).count()
    return render(request, 'countdown/countdown.html', context)
