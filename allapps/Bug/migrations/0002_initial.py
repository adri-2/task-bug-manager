# Generated by Django 5.1.7 on 2025-04-13 20:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Bug', '0001_initial'),
        ('Customers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='bugassignment',
            name='assigned_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_bugs_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bugassignment',
            name='assigned_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_bugs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bugreport',
            name='reporter_client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reported_bugs_client', to='Customers.customer'),
        ),
        migrations.AddField(
            model_name='bugreport',
            name='reporter_employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reported_bugs_employee', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bugassignment',
            name='bugs',
            field=models.ManyToManyField(related_name='assignments', to='Bug.bugreport'),
        ),
        migrations.AddField(
            model_name='bugreport',
            name='categories',
            field=models.ManyToManyField(blank=True, to='Bug.category'),
        ),
        migrations.AddField(
            model_name='bugreport',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='Bug.tags'),
        ),
    ]
