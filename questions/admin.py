from django.contrib import admin

from .models import Question, Category, Answer, BlockQuestionsModel

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Category)
admin.site.register(BlockQuestionsModel)

# Register your models here.
