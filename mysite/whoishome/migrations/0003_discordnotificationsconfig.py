# Generated by Django 3.2.15 on 2022-08-16 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whoishome', '0002_logdata_time_saved'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscordNotificationsConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled_switch', models.BooleanField(default=False)),
                ('webhook_url', models.CharField(max_length=256)),
                ('arrival_message', models.CharField(max_length=500)),
                ('departure_message', models.CharField(max_length=500)),
            ],
        ),
    ]