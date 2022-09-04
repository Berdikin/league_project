from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *

from django.views.generic import ListView, DetailView

# Create your views here.

menu = [{'title': 'Страхование +', 'url_name': 'home'},
        {'title': 'Оформить страховку', 'url_name': 'add_client'},
        {'title': 'Войти', 'url_name': 'login'},
        ]

left_menu = [{'title': 'Все страховки', 'url_name': 'home'},
             {'title': 'Все клиенты', 'url_name': 'all_clients'},
             {'title': 'Добавить клиента', 'url_name': 'add_client'},
             {'title': 'Оформить страховку', 'url_name': 'add_page'},
             {'title': 'Помощь', 'url_name': 'contact'}
             ]


class InsuranceHome(ListView):
    model = insurance
    template_name = 'insurance95/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['left_menu'] = left_menu
        context['title'] = 'Главная страница'
        return context


class ShowInsurance(DetailView):
    model = insurance
    template_name = 'insurance95/post.html'


# def index(request):
# posts = insurance.objects.all()

# context = {
# 'posts': posts,
# 'menu': menu,
# 'left_menu': left_menu,
#  'title': 'Главная страница',
#   'type_selected': 0,
# }

# return render(request, 'insurance95/index.html', context=context)


def allclients(request):
    posts = clients.objects.all()

    context = {'posts': posts,
               'menu': menu,
               'left_menu': left_menu,
               'title': 'Клиенты',
               'type_selected': 0,
               }

    return render(request, 'insurance95/allclients.html', context=context)


# def show_insurance(request, insurance_id):
#   post = get_object_or_404(insurance, insurance_id=insurance_id)

# context = {
#    'post': post,
#    'menu': menu,
#   'left_menu': left_menu,
#  'title': f'Страховка {post.insurance_id}',
#   'type_selected': post.type,
# }

# return render(request, 'insurance95/post.html', context=context)

# def show_client(request, client_id):
#   post = clients.objects.filter(client_id=client_id)

#  context = {
#      'post': post,
#      'menu': menu,
#     'left_menu': left_menu,
#        'title': f'Страховка',
#        'type_selected': post.client_id,
#    }
#    return render(request, 'insurance95/show_client', context=context)


def show_client(request, client_id):
    post = get_object_or_404(clients, client_id=client_id)
    #passport_client = passport_date.objects.filter(client_id=client__id)
    passport_client = get_object_or_404(passport_date, passport_id=client_id)

    context = {
        'post': post,
        'menu': menu,
        'left_menu': left_menu,
        'title': f'Клиент №{post.client_id}',
        'passport_client': passport_client,

    }
    return render(request, 'insurance95/show_client.html', context=context)


def post(request, insurance_id):
    return HttpResponse(f'Отображение заявки с id = {insurance_id}')


def show_type(request, type_id):
    posts = insurance.objects.filter(type_id=type_id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'left_menu': left_menu,
        'title': 'Отображение по рубрикам',
        'type_selected': type_id,
    }
    return render(request, 'insurance95/index.html', context=context)


def about(request):
    return render(request, 'insurance95/about.html', {'menu': menu, 'title': 'О сайте'})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def addclient(request):
    if request.method == 'POST':
        form = AddPassportForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect('add_page')

    else:
        form = AddPassportForm()

    return render(request, 'insurance95/addclient.html', {'form': form, 'menu': menu,
                                                          'title': 'Введите паспортные данные',
                                                          'left_menu': left_menu})


def addpage(request):
    if request.method == 'POST':
        form = AddInsuranceForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect('contact')

    else:
        form = AddInsuranceForm()

    return render(request, 'insurance95/addinsurance.html', {'form': form, 'menu': menu, 'title': 'Оформить старховку',
                                                             'left_menu': left_menu})


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")

# class LoginUser(DataMixin, LoginView):
