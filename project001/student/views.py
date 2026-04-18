from django.shortcuts import render,redirect, get_object_or_404
from .models import Student

def add_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST.get('age')
        email = request.POST.get('email')
        course = request.POST.get('course')
        Student.objects.create(
            name= name,
            age=age,
            course=course,
            email = email
        )
        return redirect('student_list')
    return render(request,'add_student.html')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html',{'students':students})

def edit_student(request,id):
    # student = Student.objects.get(id=id)
    student = get_object_or_404(Student,id=id)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.age = request.POST.get('age')
        student.email = request.POST.get('email')
        student.course = request.POST.get('course')
        student.save()
        return redirect('student_list')
    return render(request, 'edit_student.html',{'student':student})
def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('student_list')