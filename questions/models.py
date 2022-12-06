from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=63)

    def __str__(self):
        return self.category


class Answer(models.Model):
    answer = models.CharField(max_length=64)
    is_answer = models.BooleanField(default=False)
    question = models.ForeignKey("Question", on_delete=models.PROTECT)

    def is_valid_answer(self):
        return self.is_answer

    def __str__(self):
        return self.answer


class Question(models.Model):
    """Question."""

    question_title = models.CharField(max_length=127)
    cat = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.question_title


class BlockQuestionsModel(models.Model):
    name_block = models.CharField(max_length=63)
    questions = models.ManyToManyField(Question)
    cat = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.name_block
