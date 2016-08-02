# coding=utf-8
from annoying.decorators import ajax_request
from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from landing.models import Setup
from .forms import TicketForm

__author__ = 'alexy'


@ajax_request
def ticket_send(request):
    email = Setup.objects.first().email
    # email = 'od-5@yandex.ru'
    if not email:
        email = 'od-5@yandex.ru'
    if request.method == "POST":
        form = TicketForm(data=request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.status = 1
            ticket.save()
            mail_theme = u'OnlineStripClub.pro - заявка с сайта'
            message = u'Имя: %s\nТелефон: %s' % (ticket.name, ticket.phone)
            send_mail(
                mail_theme,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [email, ]
            )
    return HttpResponseRedirect(reverse('landing:thnx'))

    # return {
    #     'success': True
    # }
