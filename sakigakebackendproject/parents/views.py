from django.shortcuts import render, redirect
from .models import Parents
from .forms import ParentsUploadForm

# Create your views here.
def parents_list_view(request):
    parents = Parents.objects.all()
    return render (request, "parents/parents_list.html", {"parents": parents} )

def parents_details_view(request, id):
    parent = Parents.objects.get(id=id)
    return render(request, "parents/parent_details.html", {"parent": parent})

def parent_update_view(request, id):
    parent = Parents.objects.get(id=id)
    if request.method == "POST":
        form = ParentsUploadForm(request.POST, request.FILES, instance = parent)
        if form.is_valid():
            form.save()
            return redirect("parents_list_view")
        else:
            form = ParentsUploadForm(instance=parent)
        return render(request, "parents/edit_parent_details.html", {"form":form})
    
def remove_parent(request, id):
    parent = ParentsUploadForm.objects.get(id=id)
    parent.delete()
    return redirect("parents_list_view")