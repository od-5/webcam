# coding=utf-8
import os
from random import randint
import uuid
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, UserManager
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.core import validators
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from imagekit.models import ImageSpecField
from pilkit.processors import SmartResize
from core.files import upload_to

__author__ = 'alexy'


class MyUserManager(BaseUserManager):
    def _create_user(self, username, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, True, True,
                                 **extra_fields)

    def normalize_email(self, email):
        email = super(MyUserManager, self).normalize_email(email)
        return email.lower()


class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = u'Пользователь'
        verbose_name_plural = u'Пользователи'
        ordering = ['-date_joined']
        app_label = 'core'

    USER_TYPE_CHOICE = (
        (0, u'Суперпользователь'),
        (1, u'Администратор'),
        (2, u'Вебмастер'),
        (3, u'Сео специалист'),
        (4, u'Клиент'),
        (5, u'Менеджер'),
    )

    username = models.CharField(verbose_name=u'Имя пользователя', max_length=30, unique=True,
        help_text=_('Required. 30 characters or fewer. Letters, digits and '
                    '@/./+/-/_ only.'),
        validators=[
            validators.RegexValidator(r'^[\w.@+-]+$', _('Enter a valid username.'), 'invalid')
        ])
    email = models.EmailField(_('email address'))
    first_name = models.CharField(_('first name'), max_length=30, blank=True, null=True, default=u'')
    last_name = models.CharField(_('last name'), max_length=30, blank=True, null=True, default=u'')
    patronymic = models.CharField(u'Отчество', max_length=50, blank=True, null=True, default=u'')
    phone = models.CharField(max_length=250, verbose_name=u'Телефон', null=True, blank=True, default=u'')
    type = models.PositiveSmallIntegerField(verbose_name=u'Уровень доступа', default=0, choices=USER_TYPE_CHOICE)
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin site.'))

    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        return u'%s %s %s' % (self.last_name, self.first_name or '', self.patronymic or '')

    def get_short_name(self):
        return u'%s' % self.first_name

    def __unicode__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
