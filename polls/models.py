# -*- coding:utf-8 -*-

from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.utils import timezone


class Question(models.Model):
    """Вопрос"""
    title = models.CharField(max_length=200, verbose_name="Титул")
    text = models.TextField(verbose_name="Вопрос")
    category = models.CharField(max_length=15, null=True, verbose_name="Категория")

    def __unicode__(self):
        return self.title

        class Meta:
            verbose_name = 'Вопрос'
            verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    """Вариант ответа на вопрос"""
    question_id = models.ForeignKey(Question)
    answer = models.CharField(max_length=200, verbose_name="Ответ")
    answer_true = models.BooleanField(verbose_name="Верно?")

    def __unicode__(self):
        return self.answer

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class SaveTest(models.Model):
    user_test = models.CharField(max_length=80)
    result_question = models.TextField()
    testin_date = models.DateTimeField(default=timezone.now, null=True)
    testout_date = models.DateTimeField(blank=True, null=True)
    fio = models.CharField(max_length=80, verbose_name="ФИО", null=True)
    position = models.CharField(max_length=80, verbose_name="Должность", null=True)
