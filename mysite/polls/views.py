from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader

from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html') 
    context = {'latest_question_list': latest_question_list,}
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context) # Short version oof the above


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    ## Shortcut of the 404 response:
    # question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    # response = "You are lookgin at the result of question %s."
    # return HttpResponse(response % question_id)
    return HttpResponse("You are lookgin at the result of question %s." % question_id)


def vote(request, question_id):
    return HttpResponse("You are voting on question %s." % question_id)