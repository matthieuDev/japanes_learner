import base64, io, json

import matplotlib.image as mpimg

from django.http import HttpResponse
from django.template import loader

from japanese_learner.image_letter_classifier.model_handler import model_handler
from .models import QuestionLatin2japanese

md = model_handler()

def latin2japanese_question(request) :
    question = QuestionLatin2japanese(latin_text = 'a', japanese_text= "\u3042")
    context = { 'question' : question }

    template = loader.get_template("latin2japanese/questions.html")

    return HttpResponse(template.render(context, request))

def get_img_letter(request) :
    img = json.loads(request.body.decode('utf8'))['img']

    assert img.startswith('data:image/png;base64,')
    img = img.replace('data:image/png;base64,', '')

    img = base64.b64decode(img)
    img = io.BytesIO(img)
    img = mpimg.imread(img, format='JPG')[:,:,3] * 255

    res = md.predict(img)
    print(res)

    return res