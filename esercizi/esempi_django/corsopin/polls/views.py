from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from polls.models import Question, Choice
from pprint import pprint

def index(request):
    queryset = Question.objects.all()
    # pprint(queryset)
    # pprint(queryset[0].choices.all())
    # queryset = Question.objects.filter(question_text="test")
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    print(queryset)

    context = {
        "latest_question_list": queryset,
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    print(question_id)
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)