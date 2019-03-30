from django import forms
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.utils.timezone import now as django_now
from .models import Day


class AddDatesForm(forms.ModelForm):
    start_date = forms.DateField()
    end_date = forms.DateField()
    include_weekends = forms.BooleanField(required=False)

    class Meta:
        model = Day
        fields = ['category', 'semester', 'year']

    def clean(self):
        super(AddDatesForm, self).clean()
        start_date = self.cleaned_data.get('start_date')
        end_date = self.cleaned_data.get('end_date')
        include_weekends = self.cleaned_data.get('include_weekends')

    def save(self):
        self.instance.start_date = self.cleaned_data['start_date']
        self.instance.end_date = self.cleaned_data['end_date']
        self.instance.include_weekends = self.cleaned_data['include_weekends']
        return super(AddDatesForm, self).save()
