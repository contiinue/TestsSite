from django.contrib import admin

from .models import Question, Category, Answer

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Category)

# Register your models here.
