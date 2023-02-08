from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from power.models import Result


def index(request):

    result = Result.get_result()
    results = Result.objects.order_by('-created_at').all()

    context = {
        'results': results,
    }
    return render(request, 'power/index.html', context)
