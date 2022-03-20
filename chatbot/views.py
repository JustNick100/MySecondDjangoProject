from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.clickjacking import xframe_options_exempt
from django.core import serializers
from .models import *
import  requests
import json
# Create your views here.

@csrf_exempt
def start(request):
    if request.method == 'POST':
        chatid = request.POST.get('chatid')
        message = request.POST.get('message')
        language = request.POST.get('language')

        ischatidexist = ChatTracker.objects.filter(chatid=chatid).exists()
        if ischatidexist:
            pass
        else:
            ChatTracker(chatid=chatid).save()

        currentChat = ChatTracker.objects.filter(chatid=chatid).first()

        if message[-1]=="?":
            message = message[:-1]
        intents = message.split(" ")
        real_intent = ""

        for intent in intents:
            
            if Intent.objects.filter(name=intent.lower()).exists():
                real_intent = intent.lower()
                break

        if message in ["hi","Hi","hello","hey","Hey","Hi,there","Hello","category","Category","فئة","أهلا","مهلا"] or currentChat.status=="service":
            
            currentChat.status="category"
            currentChat.save()
            categories = []
            for category in Category.objects.all().select_related("language"):
                if category.language.name == language:
                    categories.append(category)
            return HttpResponse(serializers.serialize('json', categories), content_type="text/json-comment-filtered")
        
        elif currentChat.status=="category" or currentChat.status=="question":
            
            questions = []
            answers = []
            index=1
            if language=="English":
                index = 1
            elif language=="Arabic":
                index = 2
            
            for question in Question.objects.all():
                if question.category.intent.name==real_intent:
                    questions.append(question)
 
            if questions!=[]:
                currentChat.status="category"
                currentChat.save()
                return HttpResponse(serializers.serialize('json', questions), content_type="text/json-comment-filtered")
            
            else:            
                for answer in Answer.objects.all():
                    if answer.question.intent.name==real_intent:
                        answers.append(answer)
                currentChat.status="question"
                currentChat.save()
                return HttpResponse(serializers.serialize('json', answers), content_type="text/json-comment-filtered")
            
        else:
            return JsonResponse({"reply":None})

@csrf_exempt
def service(request):
    if request.method == 'POST':
        chatid = request.POST.get('chatid')
        language = request.POST.get('language')
        message = request.POST.get('message')

        ischatidexist = ChatTracker.objects.filter(chatid=chatid).exists()
        if ischatidexist:
            pass
        else:
            ChatTracker(chatid=chatid).save()

        currentChat = ChatTracker.objects.filter(chatid=chatid).first()
        currentChat.status = "category"
        currentChat.save()
        
        context={}
        categories = []

        for category in Category.objects.all().select_related("language"):
            if category.language.name == language:
                categories.append(category)
       
        return HttpResponse(serializers.serialize('json', categories), content_type="text/json-comment-filtered")
@csrf_exempt
def category(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        language_id = request.POST.get('language_id')
        chatid = request.POST.get('chatid')

        currentChat = ChatTracker.objects.filter(chatid=chatid).first()
        currentChat.status = "question"
        currentChat.save()

        questions = Question.objects.filter(category=category_id,language=language_id)

        return HttpResponse(serializers.serialize('json', questions), content_type="text/json-comment-filtered")

@csrf_exempt
def question(request):
    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        chatid = request.POST.get('chatid')

        currentChat = ChatTracker.objects.filter(chatid=chatid).first()
        currentChat.status = "answer"
        currentChat.save()

        answers = Answer.objects.filter(question=question_id)

        return HttpResponse(serializers.serialize('json', answers), content_type="text/json-comment-filtered")
