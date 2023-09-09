from .views import SchoolListView ,DetailView 
from django.urls  import path



urlpatterns=[
    path('schools/',SchoolListView.as_view() , name='school_list_view'),
    path('schools/<int:id>/',DetailView.as_view() , name='school_detail_view'),
    
   
 
]   
