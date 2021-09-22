from django.urls import path, include
from crudEmployee import views
urlpatterns = [
    path('showEmployees/', views.showEmployee, name="showEmployee"),
    path('insertEmployee/', views.insertEmployee, name="insertEmployee"),
    path('editEmployee/<int:id>', views.updateEmployee, name="updateEmployee"),
    path('updateEmployee/<int:id>', views.updateform, name="updateEmp"),
    path('deleteEmployee/<int:id>', views.deleteEmployee, name="deleteEmployee")
]
