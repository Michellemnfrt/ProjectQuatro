from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Repair, Car
from .forms import RepairForm, CarForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('repair_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def repair_list(request):
    repairs = Repair.objects.all()
    return render(request, 'repairs/repair_list.html', {'repairs': repairs})


def repair_detail(request, pk):
    repair = Repair.objects.get(pk=pk)
    return render(request, 'repairs/repair_detail.html', {'repair': repair})


@login_required
def repair_create(request):
    if request.method == 'POST':
        form = RepairForm(request.POST)
        if form.is_valid():
            repair = form.save()
            return redirect('repair_detail', pk=repair.pk)
    else:
        form = RepairForm()
    return render(request, 'repairs/repair_form.html', {'form': form})


@login_required
def repair_edit(request, pk):
    repair = Repair.objects.get(pk=pk)
    if request.method == "POST":
        form = RepairForm(request.POST, instance=repair)
        if form.is_valid():
            repair = form.save()
            return redirect('repair_detail', pk=repair.pk)
    else:
        form = RepairForm(instance=repair)
    return render(request, 'repairs/repair_form.html', {'form': form})


@login_required
def repair_delete(request, pk):
    Repair.objects.get(pk=pk).delete()
    return redirect('repair_list')


def car_list(request):
    cars = Car.objects.all()
    return render(request, 'repairs/car_list.html', {'cars': cars})


def car_detail(request, pk):
    car = Car.objects.get(pk=pk)
    return render(request, 'repairs/car_detail.html', {'car': car})


@login_required
def car_create(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save()
            return redirect('car_detail', pk=car.pk)
    else:
        form = CarForm()
    return render(request, 'repairs/car_form.html', {'form': form})


@login_required
def car_edit(request, pk):
    car = Car.objects.get(pk=pk)
    if request.method == "POST":
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            repair = form.save()
            return redirect('car_detail', pk=car.pk)
    else:
        form = CarForm(instance=car)
    return render(request, 'repairs/car_form.html', {'form': form})


@login_required
def car_delete(request, pk):
    Car.objects.get(pk=pk).delete()
    return redirect('car_list')

