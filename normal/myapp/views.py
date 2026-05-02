from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

def home(request):
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.hobbies = ','.join(form.cleaned_data['hobbies'])
            obj.save()
            return redirect('/')
        
    data = Student.objects.all()

    # percentage
    result = []
    for i in data:
        per = (i.gujarati + i.english) / 2
        result.append((i, per))

    return render(request, 'home.html', {'form': form, 'result': result})


def delete(request, id):
    obj = Student.objects.get(id=id)
    obj.delete()
    return redirect('/')


def update(request, id):
    person = Student.objects.get(id=id)

    hobby_list = person.hobbies.split(",")

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=person)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.hobbies = ",".join(form.cleaned_data['hobbies'])
            obj.save()
            return redirect('/')
    else:
        form = StudentForm(instance=person)
        form.fields['hobbies'].initial = hobby_list

    return render(request, 'update.html', {'form': form})