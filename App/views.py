from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Choice
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    latest_Questions=Question.objects.order_by('-pub_date')[:5]
    context={'latest_Questions':latest_Questions}
    return render(request,'App/index.html',context)


def details(request,Question_id):
    question=get_object_or_404(Question,pk=Question_id)
    return render(request,'App/details.html',{'question':question})


def result(request,Question_id):
    question=get_object_or_404(Question,pk=Question_id)
    return render(request, 'App/result.html', {'question': question})


def vote(request,Question_id):
    question=get_object_or_404(Question,pk=Question_id)
    try:
        selected_choice=question.choice_set.get(pk =request.POST['choice'])
    except:
         return render(request,'App/details.html',{'question':question,'error_message':"please select a choice"})
    else:
         selected_choice.votes+=1
         selected_choice.save()
         return HttpResponseRedirect(reverse('App:result',args=(question.id,)))

