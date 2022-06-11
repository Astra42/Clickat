from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserForm
from . import forms
from .serialyzers import CoreSerialyzer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
...
from .models import Core  # Не забудем импортировать модель Core


class Register(APIView):
    def get(self, request):
        form = UserForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            core = Core(user=user, )  # Создаем экземпляр класса Core и пихаем в него модель юзера
            core.save()  # Сохраняем изменения в базу
            return redirect('index')

        return render(request, 'register.html', {'form': form})


class Login(APIView):
    form = UserForm()

    def get(self, request):
        return render(request, 'login.html', {'form': self.form})

    def post(self, request):
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user:
            login(request, user)
            return redirect('index')
        return render(request, 'login.html', {'form': self.form, 'invalid': True})

@login_required
def user_logout(request):
    logout(request)
    return redirect("login")



@login_required
def index(request):
    core = Core.objects.get(user=request.user)
    return render(request, 'index.html', {"core":core})

@api_view(['GET'])
@login_required
def call_click(request):
    core = Core.objects.get(user=request.user)
    core.click()
    core.save()

    return Response({'core': CoreSerialyzer(core).data})
    # return render(request,  'index.html', {'core': core})




