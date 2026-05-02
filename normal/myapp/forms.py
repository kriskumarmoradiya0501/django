from django import forms
from .models import Student

class StudentForm(forms.ModelForm):

    hobbies = forms.MultipleChoiceField(
        choices=[
            ('Study', 'Study'),
            ('Travel', 'Travel'),
            ('Play', 'Play')
        ],
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Student
        fields = ['name','age','gender','hobbies','language','gujarati','english']
        widgets = {
            'gender': forms.RadioSelect(choices=[('Male','Male'),('Female','Female')]),
            'language': forms.Select(choices=[('English','English'),('Gujarati','Gujarati')])
        }