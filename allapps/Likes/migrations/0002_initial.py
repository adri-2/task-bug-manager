# Generated by Django 5.1.7 on 2025-04-13 20:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Likes', '0001_initial'),
        ('Reponsebug', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='likebugresponse',
            name='bug_response',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='Reponsebug.bugresponse'),
        ),
    ]
