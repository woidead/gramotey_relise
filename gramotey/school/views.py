from django.shortcuts import render
from school.models import Teacher, Student, Graduate, Licence
from django.http import HttpResponseRedirect


# Create your views here.
def main(request):
    licence = Licence.objects.all()
    return render(request, 'main.html', {'licence': licence} )

def for_parents(request):
    return render(request, 'for_parents/main.html')

def admission_to_School(request):
    return render(request, 'for_parents/Admission_to_School.html')

def lesson_Schedule(request):
    return render(request, 'for_parents/lesson_schedule.html')

def meeting_schedule(request):
    return render(request, 'for_parents/meeting_schedule.html')

def uniform(request):
    return render(request, 'for_parents/uniform.html')

def payment_schedule(request):
    return render(request, 'for_parents/payment_schedule.html')



def for_students_and_graduates(request):
    return render(request, 'for_students/main.html')

def for_students(request):
    return render(request, 'for_students/for_students.html')

def for_graduates(request):
    return render(request, 'for_students/for_graduates.html')



def mentors(request):
    mentors = Teacher.objects.all()
    return render(request, 'gallery/teachers.html', {'mentors': mentors})

def students(request):
    students = Student.objects.all()
    return render(request, 'gallery/students.html', {'students': students})

def graduates(request):
    graduates = Graduate.objects.all()
    
    return render(request, 'gallery/graduates.html', {'graduates': graduates})



def error_page(request):
    return render(request, 'error.html')
