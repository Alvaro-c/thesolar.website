from django.shortcuts import render
from django.http import JsonResponse

from power.models import Result, get_result


def index(request):
    get_result()
    results = Result.objects.all().order_by('-created_at')[:300]

    context = {
        'results': results,
    }
    return render(request, 'power/index.html', context)


def data(request):
    results = list(Result.objects.all().order_by('-created_at')[:300].values())

    return JsonResponse(results, safe=False)
