from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer
from .forms import StudentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


def student_list(request):
    student_list = Student.objects.all()
    paginator = Paginator(student_list, 2)  # Show 2 students per page
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        students = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results
        students = paginator.page(paginator.num_pages)
    return render(request, 'student_app/student_list.html', {'students': students})


def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)  # Include request.FILES
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_app/student_form.html', {'form': form})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)  # Include request.FILES
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_app/student_form.html', {'form': form})


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'student_app/student_confirm_delete.html', {'student': student})

