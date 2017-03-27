# -*- coding:utf-8 -*-
from django.contrib import admin
from .models import Question, Answer


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['title', 'category', 'text']
        }),
    ]

    inlines = [AnswerInline]
    list_display = ('title', 'text', 'category')
    search_fields = ['category']


admin.site.register(Question, QuestionAdmin)
