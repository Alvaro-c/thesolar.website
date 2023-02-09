from datetime import date
from datetime import datetime
from django.shortcuts import render

from power.models import Result, get_result


def index(request):
    today = date.today()
    today = datetime.combine(today, datetime.min.time())
    get_result()
    results = Result.objects.filter(created_at__gte=today).order_by('-created_at')

    context = {
        'results': results,
    }
    return render(request, 'power/index.html', context)
