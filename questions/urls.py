from django.urls import path
from .views import (
    Questions,
    NewQuestion,
    NewBlockQuestions,
    BlockQuestions,
    Registration,
    LoginUser,
    logout_user,
)

urlpatterns = [
    path("", Questions.as_view(), name="homepage"),
    path("create_question/", NewQuestion.as_view(), name="create_question"),
    path(
        "create_block_questions/",
        NewBlockQuestions.as_view(),
        name="create_block_questions",
    ),
    path("block_question/<int:pk>", BlockQuestions.as_view(), name="test"),
    path("registration/", Registration.as_view(), name="registration"),
    path("login/", LoginUser.as_view(), name="login"),
    path("logout/", logout_user, name="logout"),
]
