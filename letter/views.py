from rest_framework import generics
from .serializers import StudentsSerializer
# from django.shortcuts import render
from .models import Students
# Create your views here.

# def student_list(request):
#     students = Students.objects.all()
#     return render(request, "letter/student_list.html", {'students': students})


# def student_detail(request, pk):
#     students = Students.objects.get(id=pk)
#     return render(request, "letter/student_detail.html", {'students': students})





class StudentList(generics.ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer