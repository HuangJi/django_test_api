# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AipuAccount',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('aipu_id', models.CharField(max_length=6)),
                ('password', models.CharField(max_length=6)),
                ('wallet_user', models.CharField(max_length=100)),
            ],
        ),
    ]
