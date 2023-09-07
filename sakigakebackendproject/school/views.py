from django.shortcuts import render
from .models import School

def school_list(request):
    schools = School.objects.all()
    context = {'schools': schools}
    return render(request, 'school_list.html', context)


def school_details(request, school_id):
    school = get_object_or_404(School, school_id=school_id)
    context = {'school': school}
    return render(request, 'school_details.html', context)


def delete_school(request, school_id):
    school = get_object_or_404(School, school_id=school_id)
    
    if request.method == 'POST':
        school.delete()
        return redirect('school_list')  
    
    context = {'school': school}
    return render(request, 'delete_school_confirmation.html', context)