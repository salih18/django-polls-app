from django.http.response import Http404
from django.shortcuts import render

from .models import Question, Choice

# Get questions and display them


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def details(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')        
        
    return render(request, 'polls/details.html', {'question': question})
