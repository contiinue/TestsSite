from django import forms

from .models import Question, Answer, BlockQuestionsModel, MyUser


class NewQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ("question_title", "cat")

        widgets = {
            "question_title": forms.TextInput(attrs={"class": "form-control"}),
            "cat": forms.Select(attrs={"class": "form-control"}),
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ("answer", "is_answer", "question")

        widgets = {
            "answer": forms.TextInput(attrs={"class": "form-control"}),
            "is_answer": forms.NullBooleanSelect(attrs={"class": "form-control"}),
            "question": forms.HiddenInput(),
        }


class BlockAnswersForm(forms.ModelForm):
    questions = forms.ModelMultipleChoiceField(
        queryset=Question.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
    )

    class Meta:
        model = BlockQuestionsModel
        fields = ("name_block", "questions", "cat")

        widgets = {
            "name_block": forms.TextInput(attrs={"class": "form-control"}),
            "cat": forms.Select(attrs={"class": "form-control"}),
        }


class QuestionForm(forms.Form):
    def __init__(self, answers, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.update(
            {
                "answers": forms.ModelMultipleChoiceField(
                    queryset=answers,
                    widget=forms.SelectMultiple(attrs={"class": "form-control"}),
                )
            }
        )

    question_title = forms.CharField(
        max_length=127, widget=forms.TextInput(attrs={"class": "form-control"})
    )


class MyUserForm(forms.ModelForm):
    """Register User."""

    username = forms.CharField(
        label="Логин", widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password1 = forms.CharField(
        label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    password2 = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = MyUser
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )

        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control"}),
        }

    def save(self, commit=True):
        user = super(MyUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
