from django.urls import path
from .views import student_list, student_create, student_update, student_delete, StudentList, StudentDetail

urlpatterns = [
    path('', student_list, name='student_list'),
    path('student/new/', student_create, name='student_create'),
    path('student/<int:pk>/edit/', student_update, name='student_update'),
    path('student/<int:pk>/delete/', student_delete, name='student_delete'),
    path('api/students/', StudentList.as_view(), name='student-list'),
    path('api/students/<int:pk>/', StudentDetail.as_view(), name='student-detail'),
]
