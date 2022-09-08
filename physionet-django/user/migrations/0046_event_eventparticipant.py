# Generated by Django 3.1.14 on 2022-09-08 19:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.crypto
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0045_auto_20220528_2248'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False,
                                        verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.CharField(choices=[('Course', 'Course'),
                                                       ('Workshop', 'Workshop')],
                                              max_length=32)),
                ('added_datetime', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField(default=django.utils.timezone.now)),
                ('slug', models.SlugField(default=django.utils.crypto.get_random_string, unique=True)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                           to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': [('view_event_menu', 'Can view event menu')],
                'unique_together': {('title', 'host')},
            },
        ),
        migrations.CreateModel(
            name='EventParticipant',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False,
                                        verbose_name='ID')),
                ('added_datetime', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                            related_name='participants',
                                            to='user.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                           to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'event')},
            },
        ),
    ]
