# Generated by Django 3.2.3 on 2021-05-29 06:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_alter_jobtitle_job_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobtitle',
            name='start_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
