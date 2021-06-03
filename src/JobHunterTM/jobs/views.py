from django.shortcuts import render, HttpResponse, HttpResponseRedirect
import json

from .hunter import JobHunterTM 
from .models import JobSearchFilters
from .forms import JobSearchForm
# Create your views here.


def job_filters_view(request):
    form = JobSearchForm(request.POST or None)
    if form.is_valid():
        print('-----------------')
        form.save()
        return jobs_view(request)
    data_obj = {
        'form':form
    }   
    return render(request, "filters.html", data_obj)

def jobs_view(request, *args, **kwargs):
    filters = {
        "date": "2021-01-01",
        "ml": "hiring+jobs+machine+learning-filter:retweets",
        "ai": "hiring+jobs+artificial+intelligence-filter:retweets",
        "ds": "hiring+jobs+data+science-filter:retweets",
        "cv": "hiring+jobs+computer+vision-filter:retweets",
        "nlp": "hiring+jobs+nlp-filter:retweets"
    }

    filter_obj = JobSearchFilters.objects.last()
    obj = JobHunterTM(filter_obj.start_date)
    job = filters[filter_obj.job_title]
    result = obj.GetTweets(job)

    ## Directly throw to URL
    # result = result.to_html()
    # return HttpResponse(result)

    json_records = result.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'data_key':data}
    return render(request, "jobs.html", context)
    