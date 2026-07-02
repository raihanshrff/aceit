from django.urls import path
from .views import InterviewCreateView

urlpatterns = [
    path("",InterviewCreateView.as_view(),name="create-interview",)
]