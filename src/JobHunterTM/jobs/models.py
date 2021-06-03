from django.db import models
import datetime
# Create your models here.

JOB_CHOICES = (
    ('ml','ML'),
    ('cv', 'CV'),
    ('ds','DS'),
    ('nlp','NLP'),
)

class JobSearchFilters(models.Model):
    job_title   = models.CharField(max_length=6, choices=JOB_CHOICES, default='ml')
    start_date  = models.DateField(default=datetime.date.today)
