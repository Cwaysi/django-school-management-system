from django.shortcuts import render, redirect
from . models import *
from . forms import *
from django.contrib import messages
from datetime import datetime

def students(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully!')
            return redirect('students')
    else:
        form = StudentForm()
    context ={
        'form' : form
    }
    return render(request, 'students.html', context)

def allstudents(request):
    students = Students.objects.filter(active=True).order_by('lastname')

    context ={
        'students': students
    }
    return render (request, 'allstudents.html', context)



def attendance(request):
    today = datetime.now().date()
    attendance = Attendance.objects.filter(date__date=today).order_by('-date')
    if request.method == 'POST':
        form = AttendanceForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.cleaned_data.get('student')
            picked_by = form.cleaned_data.get('picked_by')
            timee = request.POST.get('checktime')
            if 'checkin' in request.POST:
                try:
                    stdd = Attendance.objects.get(student=student, date__date=today)
                    if stdd:
                        if stdd.check_in_time is None:
                            messages.success(request, 'Student has been already checked in today')
                            return redirect('attendance')
                        
                except Attendance.DoesNotExist:
                    stddd = Attendance()
                    stddd.year = today.year
                    stddd.month = today.month
                    stddd.student = student
                    stddd.academicYear = AcademicYear.objects.get(current=True)
                    stddd.term = Term.objects.get(current=True)
                    stddd.check_in_date = today
                    stddd.check_in_time = timee
                    stddd.checkin_by = request.user
                    stddd.save()
                    messages.success(request, 'Student has been checkedin successfully')
                    return redirect('attendance')
            else:
                try:
                    std = Attendance.objects.get(student=student, date__date=today)
                    if std:
                        if std.check_out_time is None:
                            std.check_out_date = today
                            std.check_out_time = timee
                            std.picked_by = picked_by
                            std.checkout_by = request.user
                            std.save()
                            messages.success(request, 'Student checked out successfully')
                            return redirect('attendance')
                        else:
                            messages.warning(request, 'Student has been already checked out today')
                            return redirect('attendance')
                except Attendance.DoesNotExist:
                    messages.success(request, "Student wasn't checked in today")
                    return redirect('attendance')
    else:
        form = AttendanceForm()
    context ={
        'students': attendance,
        'form' : form
    }
    return render(request, 'attendance.html', context)

def allattendance(request):
    attendance= Attendance.objects.all().order_by('-date')

    context ={
        'attendance': attendance
    }
    return render (request, 'allattendance.html', context)

