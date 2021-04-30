from django.urls import path
from . import views
from .views import Another
urlpatterns = [
    path('first', views.first),
    path('another_view', Another.as_view())
]
