from django.shortcuts import render, redirect
from .models import Students
from api.serializers import serializers

# Create your views here.
def students_list_view(request):
    students = Students.objects.all()
    return render (request, "students/", {"students": students} )

def students_details_view(request, id):
    student = Students.objects.get(id=id)
    return render(request, "students/", {"product": student})

def student_update_view(request, id):
    student = Students.objects.get(id=id)
    # if request.method == "POST":
        # serializer = StudentSerializer(request.POST, request.FILES, instance = student)
        # if form.is_valid():
        #     form.save()
        #     return redirect("students_list_view")
        # else:
        #     form = StudentSerializer(instance=student)
        # return render(request, "students/", {})
    
def remove_student(request, id):
    student = Students.objects.get(id=id)
    student.delete()
    return redirect("students_list_view")