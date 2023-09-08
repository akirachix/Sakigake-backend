
import assignment
from .models import Assignment, Notification

def create_assignment(request):
    if request.method == 'POST':
        assignment = Assignment.objects.create(
            teacher=assignment.teacher,
            title=assignment.title,
            homework=assignment.homework,
            resources=assignment.resources,
            due_date=assignment.due_date,
            date_added=assignment.date_added,
            date_updated=assignment.date_updated
        )

        parents = Parent.objects.all() 
        for parent in parents:
            preview = assignment.homework[:50] + '...' if len(assignment.homework) > 50 else assignment.homework
            notification = Notification(
                sender=assignment.teacher,
                recipient=parent,
                preview=preview,
            )
            notification.save()


