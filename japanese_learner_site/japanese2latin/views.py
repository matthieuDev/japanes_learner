from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import QuestionJapanese2latin

from japanese_learner.command_prompt_learner.french_to_katana import french_to_katana

f2k = french_to_katana()

NB_QUESTIONS_BY_TEST = 10

def japanese2latin_question(request) :
    questions = QuestionJapanese2latin.objects.order_by('?')[:NB_QUESTIONS_BY_TEST]
    context = { 'questions' : questions }

    template = loader.get_template("japanese2latin/questions.html")

    return HttpResponse(template.render(context, request))
