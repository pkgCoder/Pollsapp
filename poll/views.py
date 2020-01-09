from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def index(request):
    latest_question = Question.objects.order_by('-pub_date')[:4]
    return render(request, 'poll/index.html', {'questions':latest_question})


def detail(request ,question_id):
    details = get_object_or_404(Question, pk=question_id)
    return render(request, 'poll/detail.html', {'questions':details})

def results(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'poll/results.html', {'questions':question})



def vote(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except (KeyError , Choice.DoesNotExist):
        error = True
        return render(request, 'poll/detail.html', {'questions':question, 'error_message':error})
    else:
        selected_choice.vote += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('poll:results', args=(question_id,)))
