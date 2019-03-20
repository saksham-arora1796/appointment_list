from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('delete/<Appointment_id>', views.delete , name="delete"),
    path('cross_off/<Appointment_id>', views.cross_off , name="cross_off"),
    path('uncross/<Appointment_id>', views.uncross , name="uncross"),
    path('edit/<Appointment_id>', views.edit , name="edit"),

]
