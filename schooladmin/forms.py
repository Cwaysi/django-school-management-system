from django import forms 
from . models import *
from django.forms.widgets import DateInput, TextInput, Select, CheckboxInput

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields ='__all__'
        widgets ={
            'dob': DateInput(attrs={'type':'date','class':'forminp'}),
            'gender': Select(attrs={'class':'forminp'}),
            'current_class': Select(attrs={'class':'forminp'}),
            'firstname': TextInput(attrs={'class':'forminp'}),
            'lastname': TextInput(attrs={'class':'forminp'}),
            'middlename': TextInput(attrs={'class':'forminp'}),
            'location': TextInput(attrs={'class':'forminp'}),
            'pic': forms.ClearableFileInput(attrs={'class': 'forminp','id':'pic','onchange':'previewImage(event)','accept':'image/*'}),
            'f_fullname': TextInput(attrs={'class':'forminp'}),
            'f_occupation': TextInput(attrs={'class':'forminp'}),
            'f_mobile': TextInput(attrs={'class':'forminp'}),
            'f_address': TextInput(attrs={'class':'forminp'}),
            'f_alive': CheckboxInput(attrs={'class':'forminp'}),
            'm_fullname': TextInput(attrs={'class':'forminp'}),
            'm_occupation': TextInput(attrs={'class':'forminp'}),
            'm_address': TextInput(attrs={'class':'forminp'}),
            'm_mobile': TextInput(attrs={'class':'forminp'}),
            'm_alive': CheckboxInput(attrs={'class':'forminp'}),
            'g_fullname': TextInput(attrs={'class':'forminp'}),
            'g_occupation': TextInput(attrs={'class':'forminp'}),
            'g_address': TextInput(attrs={'class':'forminp'}),
            'g_mobile': TextInput(attrs={'class':'forminp'}),
            'formerschool': TextInput(attrs={'class':'forminp'}),
        }


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields ={'student', 'picked_by'}
        widgets ={
            'student': Select(attrs={'class':'forminp'}),
            'picked_by': TextInput(attrs={'class':'forminp'}),
        }

