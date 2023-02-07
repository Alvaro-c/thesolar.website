import os

from django.http import HttpResponse


def index(request):

    return HttpResponse("OK")


def testing(request):
    filename = './media/results/results.txt'
    with open(filename, 'r') as f:
        output = f.readlines()
        meta_tag = '<meta http-equiv="refresh" content="300">'
        css = '<style>' \
              'table {border-collapse: collapse}' \
              'td { padding-right: 20px; text-align: right ; border: 1px black solid; border-collapse: collapse' \
              '}</style>'
        result = "<table>"
        for line in output:
            line = line.replace('\n', '<br>')
            all_metrics = line.split(';')
            date_time = all_metrics[0]
            voltage = all_metrics[1]
            shunt_voltage = all_metrics[2]
            load_voltage = all_metrics[3]
            current = all_metrics[4]
            power = all_metrics[5]
            line = f"<tr><td>{date_time}</td><td>{voltage}</td><td>{shunt_voltage}</td>" \
                   f"<td>{load_voltage}</td><td>{current}</td><td>{power}</td></tr>"

            result = f"{result} {line}"
        result = f"{result} </table>"

    body = f"{meta_tag} {css} {result}"

    return HttpResponse(body)


