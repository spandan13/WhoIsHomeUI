# Generated by Django 3.2.9 on 2021-11-30 15:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_switch', models.BooleanField(default=False)),
                ('sender_address', models.CharField(max_length=100)),
                ('your_password', models.CharField(max_length=100)),
                ('to_address', models.CharField(max_length=100)),
                ('smtp_domain', models.CharField(max_length=100)),
                ('smtp_port', models.CharField(max_length=100)),
                ('departure_mail_subject', models.CharField(max_length=100)),
                ('departure_mail_body', models.CharField(max_length=500)),
                ('arrival_mail_suject', models.CharField(max_length=100)),
                ('arrival_mail_body', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mac', models.CharField(max_length=17)),
                ('ip', models.CharField(default=0, max_length=50)),
                ('first_seen', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Time last seen')),
                ('last_seen', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Time last seen')),
                ('arrival_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Last recorded arrival time')),
                ('departure_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Last recorded departure time')),
                ('scans_missed_counter', models.IntegerField(default=0)),
                ('is_home', models.BooleanField(default=False)),
                ('new', models.BooleanField(default=True)),
                ('target', models.BooleanField(default=False)),
                ('device_type', models.CharField(default='unknown', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ScannerConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('not_home_treshold', models.IntegerField()),
                ('internet_interface', models.CharField(max_length=15)),
                ('arp_string', models.CharField(max_length=100)),
                ('ip_subnet', models.CharField(max_length=100)),
                ('ip_range_start', models.CharField(max_length=100)),
                ('ip_range_end', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mac', models.CharField(max_length=17)),
            ],
        ),
        migrations.CreateModel(
            name='LogData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Check-in Time')),
                ('check_out', models.DateTimeField(blank=True, null=True, verbose_name='Check-out Time')),
                ('previous_check_out', models.DateTimeField(blank=True, null=True, verbose_name='Previous Check-Out- Time')),
                ('ip', models.CharField(default='unknown', max_length=50)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='whoishome.host')),
            ],
        ),
    ]