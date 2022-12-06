from django import forms
from .models import Question, Answer, BlockQuestionsModel


class NewQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ("question_title",)

        widgets = {
            "question_title": forms.TextInput(attrs={"class": "form-control"}),
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
