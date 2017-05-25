# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from todo.models import TodoItem

# Register your models here.
admin.site.register(TodoItem)