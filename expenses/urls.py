from django.urls import path
from . import views

urlpatterns = [
    path('', views.ExpenseListApiView.as_view(), name='expenses'),
    path('<int:id>', views.ExpenseDetailApiView.as_view(), name='expense'),
]