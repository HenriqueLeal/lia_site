from django.shortcuts import render
# from personal.models import Question
from account.models import Account

# Create your views here.

def home_screen_view(request):
    context = {}
    accounts = Account.objects.all()
    context['accounts'] = accounts


    # questions = Question.objects.all()
    # context['questions'] = questions

    '''
    
    context['some_string'] = 'this is some string que estou passando para a view'
    context['some_number'] = 34252708
    context['nome'] = "Henrique"


    context = {
        'some_string': 'segunda forma de contexto',
        'some_number': 892720,
        'nome': "Henrique",
    }

    list_of_values = []
    list_of_values.append("primeiro")
    list_of_values.append("segundo")
    list_of_values.append("terceiro")
    list_of_values.append("quarto")
    context['list_of_values'] = list_of_values
    '''
    return render(request, "personal/home.html", context)