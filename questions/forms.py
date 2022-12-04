from django import forms
from .models import Question, Answer


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
