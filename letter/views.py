from django.shortcuts import render
from .models import Students
# Create your views here.

def student_list(request):
    students = Students.objects.all()
    return render(request, "letter/student_list.html", {students: students})