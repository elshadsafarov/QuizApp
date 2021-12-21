from django.contrib import admin

from .models import Quiz, Question, Answer

admin.site.register(Quiz)


class AnswerInLine(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInLine]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
    
