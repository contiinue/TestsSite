from django.urls import path
from .views import Questions, NewQuestion

urlpatterns = [
    path("", Questions.as_view()),
    path("create_question/", NewQuestion.as_view(), name="create_question"),
]
