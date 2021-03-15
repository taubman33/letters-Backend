from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path("students/", views.StudentList.as_view(), name="student_list"),
    path('students/<int:pk>', views.StudentDetail.as_view(), name='student_detail'),
]
