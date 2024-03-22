from .  import views
from django.urls import path

urlpatterns = [
    path('', views.home, name=""),
    path('dashboard', views.dashboard, name="dashboard")
]