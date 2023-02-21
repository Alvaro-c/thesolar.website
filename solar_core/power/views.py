from django.shortcuts import render
from django.http import JsonResponse

from power.models import Result, get_battery_result, get_solar_panel_result


def index(request):
    return render(request, 'power/index.html')


def data(request):
    number_rows = request.GET.get('n', '')
    get_battery_result()
    get_solar_panel_result()

    results = [
        list(Result.objects.filter(source=Result.Source.SOLAR_PANEL)
             .order_by('-created_at')[:int(number_rows)].values()),
        list(Result.objects.filter(source=Result.Source.BATTERY)
             .order_by('-created_at')[:int(number_rows)].values())
    ]

    return JsonResponse(results, safe=False)
