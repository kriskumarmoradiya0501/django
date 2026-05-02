from django.shortcuts import render, redirect, get_object_or_404

from .models import Doctor, Appointment

from .forms import DoctorForm, AppointmentForm


# HOME PAGE
def doctor_list(request):

    doctors = Doctor.objects.all()

    return render(request, 'doctor_list.html', {
        'doctors': doctors
    })


# ADD DOCTOR
def add_doctor(request):

    form = DoctorForm(request.POST or None)

    if form.is_valid():

        form.save()

        return redirect('doctor_list')

    return render(request, 'add_doctor.html', {
        'form': form
    })


# DOCTOR DETAIL
def doctor_detail(request, doctor_id):

    doctor = get_object_or_404(Doctor, id=doctor_id)

    appointments = Appointment.objects.filter(doctor=doctor)

    return render(request, 'doctor_detail.html', {
        'doctor': doctor,
        'appointments': appointments
    })


# BOOK APPOINTMENT
def book_appointment(request, doctor_id):

    doctor = get_object_or_404(Doctor, id=doctor_id)

    form = AppointmentForm(request.POST or None)

    if form.is_valid():

        appointment = form.save(commit=False)

        appointment.doctor = doctor

        appointment.save()

        return redirect('doctor_list')

    return render(request, 'book_appointment.html', {
        'form': form,
        'doctor': doctor
    })