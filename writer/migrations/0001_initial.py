# Generated by Django 3.1.7 on 2021-03-12 16:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=1500)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('sent', models.BooleanField(default=False)),
                ('send_attempt_over', models.BooleanField(default=False)),
            ],
        ),
    ]
