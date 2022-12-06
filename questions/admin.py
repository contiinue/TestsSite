from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Question, Category, Answer, BlockQuestionsModel, MyUser

admin.site.register(MyUser, UserAdmin)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Category)
admin.site.register(BlockQuestionsModel)

# Register your models here.
