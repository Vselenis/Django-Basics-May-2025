# Generated by Django 5.2.3 on 2025-06-22 06:57

import django.core.validators
import organizers.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(help_text='*Allowed names contain letters, digits, spaces, and hyphens.', max_length=110, unique=True, validators=[django.core.validators.MinLengthValidator(2), organizers.models.validate_company_name])),
                ('phone_number', models.CharField(max_length=15, unique=True, validators=[organizers.models.validate_phone_number])),
                ('secret_key', models.CharField(help_text='*Pick a combination of 4 unique digits.', max_length=4, validators=[organizers.models.validate_secret_key])),
                ('website', models.URLField(blank=True, null=True)),
            ],
            options={
                'constraints': [models.UniqueConstraint(fields=('phone_number',), name='unique_phone_number', violation_error_message='That phone number is already in use!')],
            },
        ),
    ]
