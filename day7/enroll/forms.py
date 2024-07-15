from django import forms

class StudentRegistration(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    topic=forms.CharField(label='Your Subject', help_text='Enter your topic')
    file=forms.FileField()
