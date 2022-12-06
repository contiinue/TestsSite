from django.urls import path
from .views import Questions, NewQuestion, NewBlockQuestions, BlockQuestions

urlpatterns = [
    path("", Questions.as_view()),
    path("create_question/", NewQuestion.as_view(), name="create_question"),
    path(
        "create_block_questions/",
        NewBlockQuestions.as_view(),
        name="create_block_questions",
    ),
    path("block_question/<int:pk>", BlockQuestions.as_view()),
]
