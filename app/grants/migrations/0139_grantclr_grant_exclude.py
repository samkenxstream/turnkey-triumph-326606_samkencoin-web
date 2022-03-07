# Generated by Django 2.2.24 on 2022-03-07 10:01

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0138_granttag_is_eligibility_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='grantclr',
            name='grant_exclude',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text='Grants excluded in this CLR round', null=True),
        ),
    ]
