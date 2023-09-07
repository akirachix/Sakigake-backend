from django.shortcuts import render, redirect
from .models import Students
from .forms import StudentUploadForm

# Create your views here.
def students_list_view(request):
    students = Students.objects.all()
    return render (request, "students/students_list.html", {"students": students} )

def students_details_view(request, id):
    student = Students.objects.get(id=id)
    return render(request, "students/student_details.html", {"product": student})

def student_update_view(request, id):
    student = Students.objects.get(id=id)
    if request.method == "POST":
        form = StudentUploadForm(request.POST, request.FILES, instance = student)
        if form.is_valid():
            form.save()
            return redirect("students_list_view")
        else:
            form = StudentUploadForm(instance=student)
        return render(request, "students/edit_student_details.html", {"form":form})
    
def remove_student(request, id):
    student = Students.objects.get(id=id)
    student.delete()
    return redirect("students_list_view")