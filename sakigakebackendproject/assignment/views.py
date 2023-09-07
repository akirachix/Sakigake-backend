import requests
from django.shortcuts import render, redirect, get_object_or_404
from .models import Assignment
from .forms import AssignmentForm  


def fetch_assignments(request):

    api_url = ''
    
    
    response = requests.get(api_url)
    
    if response.status_code == 200:
        assignments_data = response.json()  
        
        for assignment_data in assignments_data:
            assignment, created = Assignment.objects.update_or_create(
                homework=assignment_data['homework'],  
                defaults={
                    'subject': assignment_data['subject_id'],  
                    'resources': assignment_data['resources'],
                    'due_date': assignment_data['due_date'],
                    'date_added': assignment_data['date_added'],
                    'date_updated': assignment_data['date_updated'],
                }
            )
    
    # assignments = Assignment.objects.all()
    # return render(request, 'assignments.html', {'assignments': assignments})

def add_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            assignment = form.save()
            api_url = ''
            api_data = {
                'subject_id': assignment.subject.id,
                'homework': assignment.homework,
                'resources':assignment.resources
            }
            response = requests.post(api_url, json=api_data)
            if response.status_code == 201:  
                return redirect('fetch_assignments')
    else:
        form = AssignmentForm()
    return render(request, 'add_assignment.html', {'form': form})

def edit_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    
    if request.method == 'POST':
        form = AssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            form.save()
            return redirect('fetch_assignments')
    else:
        form = AssignmentForm(instance=assignment)
    
    # return render(request, 'edit_assignment.html', {'form': form, 'assignment': assignment})

def delete_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    
    if request.method == 'POST':
        assignment.delete()
        return redirect('fetch_assignments') 
    
    # return render(request, 'delete_assignment.html', {'assignment': assignment})
