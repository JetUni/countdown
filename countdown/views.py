from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404, render

from .forms import AddDatesForm
from .models import *


def index(request, category_id=1):
    context = {}
    category = get_object_or_404(Category, pk=category_id)
    today = datetime.now().date()
    if category.name == "School":
        for s in Semester.objects.all():
            if s.start <= today and s.end >= today:
                semester = s
        total_days = Day.objects.filter(
            category_id=category_id,
            semester=semester,
            year=datetime.now().year
        ).count()
        days_left = Day.objects.filter(
            category_id=category_id,
            semester=semester,
            year=datetime.now().year,
            date__gt=datetime.now()
        ).count()
        context['title'] = "{} {}".format(semester, datetime.now().year)
    else:
        total_days = Day.objects.filter(category_id=category_id).count()
        days_left = Day.objects.filter(
            category_id=category_id, date__gt=datetime.now()).count()
        context['title'] = category.name

    context['category'] = category
    context['total_days'] = total_days
    context['days_left'] = days_left

    return render(request, 'countdown/countdown.html', context)


def add_dates(request):
    if request.method == 'GET':
        form = AddDatesForm
        return render(request, 'countdown/dates.html', {'form': form})
    else:
        form = AddDatesForm(request.POST)
        if form.is_valid():
            include_weekends = form.cleaned_data['include_weekends']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            category = form.cleaned_data['category']
            semester = form.cleaned_data['semester']
            year = form.cleaned_data['year']
            diff = end_date - start_date + timedelta(days=1)
            dates = []
            for i in range(diff.days):
                day = start_date + timedelta(days=i)
                if include_weekends:
                    dates.append(day)
                elif day.weekday() != 5 and day.weekday() != 6:
                    dates.append(day)
            for day in dates:
                Day.objects.create(category=category, semester=semester,
                                   year=year, date=day)
            return render(request, 'countdown/dates.html',
                          {'form': AddDatesForm})
