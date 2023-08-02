from . import views
from django.urls import path
app_name = 'TodoApp'
urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:taskId>/', views.deleteTask, name='delete'),
    path('update/<int:taskId>/', views.updateData, name='update'),
    path('listview/', views.TaskListView.as_view(), name='listview'),
    path('detailview/<int:pk>/', views.TaskDetailView.as_view(), name='detailview'),
    path('updateview/<int:pk>/', views.TaskUpdateView.as_view(), name='updateview'),
    path('deleteview/<int:pk>/', views.TaskDeleteView.as_view(), name='deleteview'),
]