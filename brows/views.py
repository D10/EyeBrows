from django.contrib import messages
from django.db.models import Q
from django.http import QueryDict
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.contrib.auth import login, logout
from django.views.generic import ListView, DetailView
from django.middleware.csrf import get_token
from django.core.files.base import ContentFile
from django.core.paginator import Paginator

import brows.forms
from .forms import SendMailForm, UserLoginForm
from .sendmail import send_name, password_generator
from .models import Lessons, Answers, Photos


def home(request):
    return render(request, 'index.html')


def user_contact(request):
    if request.method == 'POST':
        form = SendMailForm(request.POST)
        if form.is_valid():
            csrf_token = get_token(request)
            password = password_generator()
            email = form.cleaned_data['mail']
            user = brows.forms.UserRegisterForm({'csrfmiddlewaretoken': [csrf_token], 'username': email, 'email': email,
                                                 'password1': password, 'password2': password})
            user = user.save()
            mail = send_mail('Заказ в школе бровистов', send_name(form.cleaned_data['name'], email, password),
                             'bogdan1414let@gmail.com', [email], fail_silently=True)
            if mail:
                messages.success(request, 'Письмо с авторизационными данными отправлено на Ваш email')
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Ошибка отправки. Попробуйте еще раз')
        else:
            messages.error(request, 'Данные введены неправильно. Попробуйте еще раз')
    else:
        form = SendMailForm()
    return render(request, 'email.html', {'form': form})


class LessonsDetail(DetailView):
    model = Lessons
    template_name = 'brows/lesson_detail.html'
    context_object_name = 'lessons'


def lessons_detail(request, pk):
    lesson_item = get_object_or_404(Lessons, pk=pk)
    lessons_nav = Lessons.objects.all()
    prev_lesson = Lessons.objects.filter(pk__lt=pk).order_by('-pk').first()
    lesson_previous = Answers.objects.filter(
        Q(user_answer=request.user) & Q(from_lesson=prev_lesson)
    ).first()
    if request.method == 'POST':
        images = request.FILES.getlist('photos')
        answer = Answers.objects.create(user_answer=request.user, from_lesson=lesson_item,
                                        is_correct=False)
        for image in images:
            Photos.objects.create(
                image=image,
                answer=answer
            )
    return render(request, 'brows/lesson_detail.html', {'lessons': lesson_item,
                                                        'lessons_nav': lessons_nav,
                                                        'lesson_previous': lesson_previous
                                                        })


def lessons_list(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('lessons_list')
    else:
        form = UserLoginForm()
    lessons = Lessons.objects.order_by('pk')
    return render(request, 'brows/lessons_list.html', {'lessons': lessons,
                                                       'form': form})


def user_logout(request):
    logout(request)
    return redirect('lessons_list')
