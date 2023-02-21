from django.shortcuts import render
from django.http import JsonResponse

from power.models import Result, get_result


def index(request):
    return render(request, 'power/index.html')


def data(request):
    number_rows = request.GET.get('n', '')
    get_result()

    results = list(Result.objects.all().order_by('-created_at')[:int(number_rows)].values())

    return JsonResponse(results, safe=False)
