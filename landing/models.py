# coding=utf-8
from django.db import models
from core.base_model import Common
from core.models import User

__author__ = 'alexy'


class Setup(models.Model):
    class Meta:
        verbose_name = u'Настройки сайта'
        verbose_name_plural = u'Настройки сайта'
        app_label = 'landing'

    def __unicode__(self):
        if self.title:
            return self.title
        else:
            return u'Настройки'

    title = models.CharField(verbose_name=u'Заголовок <TITLE>...</TITLE>', max_length=256, blank=True)
    email = models.EmailField(verbose_name=u'e-mail для приёма заявок', blank=True)
    meta_key = models.TextField(verbose_name=u'Ключевые слова META_KEYWORDS', blank=True)
    meta_desc = models.TextField(verbose_name=u'Описание META_DESCRIPTION', blank=True)
    top_js = models.TextField(verbose_name=u'Скрипты в <HEAD>..</HEAD>', blank=True)
    bottom_js = models.TextField(verbose_name=u'Скрипты перед закрывающим </BODY>', blank=True)
    robots_txt = models.TextField(verbose_name=u'ROBOTS.TXT', blank=True, null=True)
    sitemap = models.TextField(verbose_name=u'sitemap.xml', blank=True, null=True)


class Ticket(Common):
    class Meta:
        verbose_name = u'Заявка'
        verbose_name_plural = u'Заявки'
        app_label = 'landing'

    def __unicode__(self):
        return self.name

    def performed_at(self):
        pass

    TICKET_STATUS_CHOICE = (
        (0, u'В обработке'),
        (1, u'Новая заявка'),
        (2, u'Отклонена'),
        (3, u'Нет ответа'),
    )

    manager = models.ForeignKey(to=User, verbose_name=u'Менеджер', blank=True, null=True)
    name = models.CharField(verbose_name=u'Имя', max_length=256)
    phone = models.CharField(verbose_name=u'Телефон', max_length=20)
    status = models.PositiveSmallIntegerField(verbose_name=u'Статус заявки',  choices=TICKET_STATUS_CHOICE, default=1)
    comment = models.TextField(verbose_name=u'Комментарий менеджера', blank=True, null=True)
    sale = models.BooleanField(verbose_name=u'Продажа', default=False)
    price = models.PositiveIntegerField(verbose_name=u'Сумма', blank=True, null=True)
    country = models.CharField(max_length=200, verbose_name=u'Страна', blank=True, null=True)
    city = models.CharField(max_length=200, verbose_name=u'Город', blank=True, null=True)
    contact_date = models.DateField(verbose_name=u'Дата контакта', blank=True, null=True)
