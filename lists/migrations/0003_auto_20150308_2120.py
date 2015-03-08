# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_auto_20150301_1937'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ('created_at',)},
        ),
        migrations.AlterModelOptions(
            name='todolist',
            options={'ordering': ('created_at',)},
        ),
        migrations.AlterField(
            model_name='todo',
            name='creator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, related_name='todos'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='todo',
            name='todolist',
            field=models.ForeignKey(to='lists.TodoList', related_name='todos'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='todolist',
            name='creator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, related_name='todolists'),
            preserve_default=True,
        ),
    ]
