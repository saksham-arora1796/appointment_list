from django.shortcuts import render, redirect
from .models import Appointment
from .forms import AppointmentForm
from django.contrib import messages


def home(request):
    request.method == 'POST'                                                    #If an Appointment is to be scheduled the we add it from here.
    form = AppointmentForm(request.POST or None)

    if form.is_valid():
        form.save()
        all_items = Appointment.objects.all
        messages.success(request, ('Your Appointment has been scheduled!!'))
        return render(request, 'home.html', {'all_items': all_items})

    else:
        all_items= Appointment.objects.all                                  #Otherwise we just show the already scheduled Appointments
        return render(request, 'home.html', {'all_items': all_items})


def delete(request, Appointment_id):
    item = Appointment.objects.get(pk=Appointment_id)
    item.delete()
    messages.success(request,('This Appointment has been removed! Please Schedule another Appointment!!'))
    return redirect('home')

def cross_off(request, Appointment_id):
    item = Appointment.objects.get(pk=Appointment_id)
    item.completed = True
    item.save()
    return redirect('home')

def uncross(request, Appointment_id):
    item = Appointment.objects.get(pk=Appointment_id)
    item.completed = False
    item.save()
    return redirect('home')

def edit(request, Appointment_id):
    if request.method == 'POST':
        item = Appointment.objects.get(pk=Appointment_id)

        form = AppointmentForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ('Your Appointment has been edited! Please be on time!!'))
            return redirect('home')

    else:
        item = Appointment.objects.get(pk=Appointment_id)
        return render(request, 'edit.html', {'item':item})
