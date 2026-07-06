from django.urls import path
from .views import InterviewCreateView,QuestionCreateView,SubmitAnswerView

urlpatterns = [
    path("",InterviewCreateView.as_view(),name="create-interview"),
    path("<int:interview_id>/questions/",QuestionCreateView.as_view(),name="question_list"),
    path("answers/",SubmitAnswerView.as_view(),name="submit-answer"),
]