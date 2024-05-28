from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Usuarios

# Create your views here.

def welcome(request):
    my_users = Usuarios.objects.all().values()
    template = loader.get_template('users.html')
    context = {
        'my_users':my_users,
    }
    return HttpResponse(template.render(context, request))


def test(request):
    return render(request, '../templates/test.html')