from django.db.models import QuerySet
from django.http import HttpResponse
from django.views.generic import ListView, FormView
from .forms import NewQuestionForm, AnswerForm, BlockAnswersForm, QuestionForm
from django.urls import reverse_lazy

from .get_stats_of_user_answer import get_stats_of_user_answer
from .utils import save_answer
from .models import BlockQuestionsModel
from formtools.wizard.views import SessionWizardView
from collections import OrderedDict


class Questions(ListView):
    template_name = "questions/questions.html"
    queryset = BlockQuestionsModel.objects.all()
    context_object_name = "question_block"

    def get_queryset(self):
        block_questions = super().get_queryset()
        category = self.request.GET.get("category")
        if not category:
            return block_questions
        return block_questions.filter(cat=category)


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


class NewBlockQuestions(FormView):
    form_class = BlockAnswersForm
    template_name = "questions/new_block_questions.html"
    success_url = reverse_lazy("create_block_questions")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class BlockQuestions(SessionWizardView):
    form_list = [QuestionForm]
    template_name = "questions/block_question.html"

    def get_form(self, step=None, data=None, files=None):
        """Get form(question and his answers) by step."""
        if step is None:
            step = self.steps.current
        all_questions_of_block = self.get_all_questions()

        question_of_step = all_questions_of_block[int(step)]
        form_class = self.get_form_list(all_questions_of_block.count())[step]

        kwargs = self.get_form_kwargs(step, question_of_step)
        kwargs.update(
            {
                "data": data,
                "files": files,
                "prefix": self.get_form_prefix(step, form_class),
                "initial": self.get_form_initial(step, question_of_step),
            }
        )
        return form_class(**kwargs)

    def get_all_questions(self) -> QuerySet[Questions]:
        return (
            BlockQuestionsModel.objects.select_related("cat")
            .get(pk=self.kwargs["pk"])
            .questions.all()
        )

    def get_form_list(self, count_question_of_block=None):
        """Get forms by question block."""
        if count_question_of_block:
            self.form_list = OrderedDict()
            count_question = [QuestionForm for _ in range(count_question_of_block)]
            for i, form in enumerate(count_question):
                self.form_list[str(i)] = form
        return super().get_form_list()

    def get_form_initial(self, step, question_of_step=None):
        """Return question title."""
        return {"question_title": question_of_step.question_title}

    def get_form_kwargs(self, step=None, question_of_step=None):
        """Return Variants answer of question if step is True."""
        if step and question_of_step:
            return {
                "answers": question_of_step.answer_set.select_related(
                    "question"
                ).all()
            }
        return super().get_form_kwargs(step)

    def done(self, form_list, **kwargs):
        return HttpResponse(get_stats_of_user_answer(form_list))
