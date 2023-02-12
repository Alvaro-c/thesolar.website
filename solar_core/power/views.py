from datetime import date
from datetime import datetime
from django.shortcuts import render

from power.models import Result, get_result


def index(request):
    today = date.today()
    today = datetime.combine(today, datetime.min.time())
    # get_result()
    results = Result.objects.all().order_by('-created_at')[:300]

    context = {
        'results': results,
    }
    return render(request, 'power/index.html', context)
