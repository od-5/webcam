# coding=utf-8
from annoying.decorators import ajax_request
from annoying.functions import get_object_or_None
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import UpdateView, TemplateView
from core.models import User

__author__ = 'alexy'


class WelcomeView(TemplateView):
    template_name = 'cabinet/welcome.html'

    def get_context_data(self, **kwargs):
        context = super(WelcomeView, self).get_context_data()
        try:
            usertype = int(self.request.GET.get('usertype'))
        except:
            usertype = 1
        context.update({
            'usertype': usertype
        })
        return context


def cabinet_sign(request):
    context = {}
    try:
        usertype = int(request.GET.get('usertype'))
    except:
        usertype = 1
    error = None
    # if request.user.is_authenticated():
    #     return HttpResponseRedirect(reverse('administrator:list'))
    # else:
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        usercheck = get_object_or_None(User, username=username, type=usertype)
        if usercheck:
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if user.type == 1:
                        return HttpResponseRedirect(reverse('cabinet:administrator:dashboard'))
                    elif user.type == 2:
                        return HttpResponseRedirect(reverse('cabinet:webmaster:dashboard'))
                    elif user.type == 3:
                        return HttpResponseRedirect(reverse('cabinet:seo:dashboard'))
                else:
                    error = u'Пользователь заблокирован'
            else:
                error = u'Пожалуйста, введите корректные Имя пользователя и пароль для аккаунта. Оба поля могут быть чувствительны к регистру.'
        else:
            if usertype == 1:
                error_name = u'Администратора'
            elif usertype == 2:
                error_name = u'Вебмастера'
            elif usertype == 3:
                error_name = u'Сео специалиста'
            else:
                error_name = u'Пользователя'
            error = u'%s с таким логином не зарегистрировано в системе. Проверьте правильность ввода даных.' % error_name
    context.update({
        'usertype': usertype,
        'error': error
    })
    return render(request, 'cabinet/welcome.html', context)
