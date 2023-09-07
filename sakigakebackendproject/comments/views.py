from django.shortcuts import redirect, render
from .forms import CommentUploadForm
from .models import Comment

def upload_comment(request):
    if request.method == "POST":
        form=CommentUploadForm(request.POST,request.FILES)
        if form.is_valid():
         comment = form.save(commit=False)
         comment.save()
    else:
        form = CommentUploadForm()
        
    return render (request,'comments/comment_upload.html',{'form':form})

def comments_list(request):
    comments = Comment.objects.all()
    return render (request,"comments/comment_list.html",{"comments":comments})

        
def edit_comment(request,id):
    comment = Comment.objects.get(id=id)
    if request.method == "POST":
        form = CommentUploadForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            
            return redirect("comment_list_view", id= comment.id)
    else:
        form = CommentUploadForm(instance=comment)
        return render(request, "comments/edit_comment.html",{"form":form})  
 
def delete_comment(request,id):
    comment = Comment.objects.get(id=id)
    if request.method == "POST":
        comment.delete()
        return redirect('comments_list_view')
    return render(request, "comments/delete_comment.html", {"comment":comment} )
        
