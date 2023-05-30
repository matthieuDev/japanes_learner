from django.http import HttpResponse
from django.template import loader

from .models import QuestionLatin2japanese

def latin2japanese_question(request) :
    question = QuestionLatin2japanese(latin_text = 'a', japanese_text= "\u3042")
    context = { 'question' : question }

    template = loader.get_template("latin2japanese/questions.html")

    return HttpResponse(template.render(context, request))
