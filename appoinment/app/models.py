from django.db import models


class Doctor(models.Model):

    name = models.CharField(max_length=100)

    specialization = models.CharField(max_length=100)

    qualification = models.CharField(max_length=100)

    experience = models.IntegerField()

    fees = models.DecimalField(max_digits=8, decimal_places=2)

    email = models.EmailField()

    phone = models.CharField(max_length=15)

    available = models.BooleanField(default=True)

    joining_date = models.DateField()

    bio = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Appointment(models.Model):

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    patient_name = models.CharField(max_length=100)

    patient_email = models.EmailField()

    contact_number = models.CharField(max_length=15)

    gender = models.CharField(max_length=10)

    age = models.IntegerField()

    appointment_date = models.DateField()

    symptoms = models.TextField()

    emergency = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient_name