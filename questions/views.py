from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .forms import NewQuestionForm, AnswerForm
from django.urls import reverse_lazy
from .utils import save_answer


class Questions(TemplateView):
    template_name = "questions/questions.html"


class NewQuestion(FormView):
    form_class = NewQuestionForm
    template_name = "questions/new_question.html"
    success_url = reverse_lazy("create_question")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["answer_form"] = [AnswerForm() for _ in range(2)]
        return context

    def form_valid(self, form):
        question_model = form.save()
        self.validate_answer_form(question_model.pk)
        return super().form_valid(form)

    def validate_answer_form(self, question_pk: int) -> None:
        """Save answers"""
        answer, is_answer = self.request.POST.getlist(
            "answer"
        ), self.request.POST.getlist("is_answer")
        for ans, is_val in zip(answer, is_answer):
            save_answer(
                AnswerForm(
                    data={"answer": ans, "is_answer": is_val, "question": question_pk}
                )
            )
