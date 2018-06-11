from django.contrib import admin
from .models import *


class DayAdmin(admin.ModelAdmin):
    list_display = ('date', 'category', 'semester', 'year')
    list_filter = ('category', 'semester', 'year')


admin.site.register(Category)
admin.site.register(Semester)
admin.site.register(Day, DayAdmin)
