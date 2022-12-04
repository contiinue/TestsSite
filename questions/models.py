from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=63)
    is_valid = models.BooleanField(default=False)


class Answer(models.Model):
    answer = models.CharField(max_length=64)


class Question(models.Model):
    """Question by category."""

    question_title = models.CharField(max_length=127)
    answers = models.ManyToManyField(Answer)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
