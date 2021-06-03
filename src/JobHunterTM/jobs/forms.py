from django import forms
from .models import JobSearchFilters

class JobSearchForm(forms.ModelForm):
    class Meta:
        model = JobSearchFilters
        fields = [
            'job_title',
            'start_date'
        ]   

    def clean_title(self, *args, **kwargs):
        job = self.cleaned_data.get('job_title')
        print('title clean')
        return job

    def clean_date(self, *args, **kwargs):
        date = self.cleaned_data.get('start_date')
        print('date clean')
        return date