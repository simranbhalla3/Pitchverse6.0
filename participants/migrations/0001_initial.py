# Generated by Django 4.0.2 on 2022-02-08 08:15

import django.core.validators
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PreEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Team_name', models.CharField(max_length=100)),
                ('Member1_name', models.CharField(max_length=50)),
                ('Member1_email', models.EmailField(max_length=254, unique=True, verbose_name='Email Address')),
                ('Member1_contact_no', phonenumber_field.modelfields.PhoneNumberField(help_text='Add country code before the contact no.', max_length=128, region=None)),
                ('Member1_roll_no', models.CharField(default=' ', help_text='Enter your Roll No. if you are studying in TIET otherwise enter your college name', max_length=100, verbose_name='Roll no/ College Name')),
                ('Member1_are_you_a_thapar_student', models.BooleanField(default=True, verbose_name='Are you a thapar student?')),
                ('Member1_year_of_study', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('Member1_discordid', models.CharField(max_length=100)),
                ('Member2_name', models.CharField(blank=True, max_length=50)),
                ('Member2_email', models.EmailField(blank=True, max_length=254, verbose_name='Email Address')),
                ('Member2_contact_no', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Add country code before the contact no.', max_length=128, region=None)),
                ('Member2_roll_no', models.CharField(blank=True, default=' ', help_text='Enter your Roll No. if you are studying in TIET otherwise enter your college name', max_length=100, verbose_name='Roll no/ College Name')),
                ('Member2_are_you_a_thapar_student', models.BooleanField(blank=True, default=True, verbose_name='Are you a thapar student?')),
                ('Member2_year_of_study', models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('Member2_discordid', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]