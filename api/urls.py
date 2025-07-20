from django.urls import path
from .import views
urlpatterns = [
 path('students/',views.studentviews),
 path('update/<int:pk>/',views.update)   
]
