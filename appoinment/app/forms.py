from django import forms

from .models import Doctor, Appointment


class DoctorForm(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = '__all__'


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = '__all__'