from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:category_id>/', views.index, name='count_by_category'),
]
