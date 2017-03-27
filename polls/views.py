# -*- coding:utf-8 -*-
#import pdb;pdb.set_trace()

from django.shortcuts import render
from .forms import RegisterFormView, LoginFormView, LogoutView
from .models import Question, Answer, SaveTest
from django.shortcuts import redirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def Testing(request):

    if not request.user.is_authenticated:
        return render(request, 'polls/logout.html')
    else:
        username = str(request.user)
        if 'chiefs1' in username:
            user_category = 'chiefs1'
            questions = Question.objects.filter(category=user_category).order_by('?')[:2]
        elif 'chiefs2' in username:
            user_category = 'chiefs2'
            questions = Question.objects.filter(category=user_category).order_by('?')[:2]
        elif 'clerkc1' in username:
            user_category = 'clerkc1'
            questions = Question.objects.filter(category=user_category).order_by('?')[:2]
        elif 'clerkc2' in username:
            user_category = 'clerkc2'
            questions = Question.objects.filter(category=user_category).order_by('?')[:2]
        elif 'registar1' in username:
            user_category = 'registar1'
            questions = Question.objects.filter(category=user_category).order_by('?')[:2]
        elif 'registar2' in username:
            user_category = 'registar2'
            questions = Question.objects.filter(category=user_category).order_by('?')[:2]
        else:
            questions = Question.objects.order_by('?')[:4]

        #questions = Question.objects.order_by('?')[:2]
        #username = request.user  #.username
        testin_date = timezone.now()
        data = ''

        if request.POST.get('answer'):
            data = request.POST.getlist('answer', [])
            if 'fio' in request.POST:
                fio = request.POST.get('fio', '')
            if 'position' in request.POST:
                position = request.POST.get('position', '')
            testout_date = timezone.now()
            addbd = SaveTest(
                user_test=username,
                result_question=data,
                testin_date=testin_date,
                testout_date=testout_date,
                fio=fio, position=position)
            addbd.save()
            return redirect('result')

        return render(request, 'polls/index.html',
                      {'questions': questions,
                       'username': username})


@csrf_protect
def ValidateQuestionAnswers(request):
    username = request.user
    if not request.user.is_authenticated:
        return render(request, 'polls/logout.html')
    else:
        username = request.user
        true_answer = Answer.objects.filter(answer_true=1)
        #user_answer_quest = SaveTest.objects.all().latest('testout_date')
        user_answer_quest = SaveTest.objects.filter(user_test=username).latest('testout_date')
        user_answer = user_answer_quest.result_question
        name_quest = SaveTest.objects.filter(user_test=username).latest('testout_date')
        fio = name_quest.fio
        position = name_quest.position

        if user_answer:

            req = ["u", "\'", "[", " ", "]"]
            answer = {}

            for i in range(0, len(req)):
                re = req[i]
                user_answer = user_answer.replace(re, '')
            user_answer = [el for el in user_answer.split(",")]
            #print '->', user_answer
            for el in user_answer:
                el0 = int(el[0])
                el2 = str(el[2])
                e = {el0: el2}
                if el0 in answer:
                    a = answer.get(el0)
                    e = {el0: el2 + str(a)}
                    answer.update(e)
                else:
                    answer.update(e)

        if true_answer:
            etalon_answer = {}

            for result in true_answer:
                r = {result.question_id_id: str(result.id)}

                if result.question_id_id in etalon_answer:
                    a = etalon_answer.get(result.question_id_id)
                    r = {result.question_id_id: str(result.id) + ',' + str(a)}
                    etalon_answer.update(r)
                else:
                    etalon_answer.update(r)

        summa_true_answer = 0
        summa_false_answer = 0
        answer_values = [] #ответы юзера
        for key, value in etalon_answer.items():
            if answer.get(key):
                a = answer.get(key)
                if len(a) < 2:
                    answer_values.append(int(a))
                    if a in value:
                        summa_true_answer = summa_true_answer + 1
                    else:
                        summa_false_answer = summa_false_answer + 1
                else:
                    for ans in a:
                        answer_values.append(int(ans))
                        if ans in value:
                            summa_true_answer = summa_true_answer + 1
                        else:
                            summa_false_answer = summa_false_answer + 1

        print 'answer --->', answer
        print 'etalon_answer --->', etalon_answer

        all_questions = Question.objects.all()
        answer_key = answer.keys()

        print 'answer_key --->', answer_key
        print 'answer_values --->', answer_values

        return render(request, 'polls/result.html', {
            'summa_true_answer': summa_true_answer,
            'summa_false_answer': summa_false_answer,
            'answer_key': answer_key,
            'answer_values': answer_values,
            'all_questions': all_questions,
            'fio': fio,
            'position': position,
        })
