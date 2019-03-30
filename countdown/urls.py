from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:category_id>/', views.index, name='count_by_category'),
    path('dates/', views.add_dates, name='add_dates'),
]
