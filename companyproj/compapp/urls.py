from django.urls import path
from . import views

urlpatterns = [
    path('employee_list/', views.employee_view,
         name= 'employee_list'),
]
