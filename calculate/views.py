from django.shortcuts import render
from calculate.models import Calculate
def calculate(request):
    list = Calculate.objects.all()
    if request.method == "POST":
        boom = request.POST
        first_number = int(boom['first_number'])
        second_number = int(boom['second_number'])
        summa = int(boom['first_number']) + int(boom['second_number'])
        minus = int(boom['first_number']) - int(boom['second_number'])
        multiply = int(boom['first_number']) * int(boom['second_number'])
        if int(boom['second_number']) == 0:
            division = 0
        else:
            division = int(boom['first_number']) / int(boom['second_number'])
        obj_db = Calculate(first_number=int(boom['first_number']),
                      second_number=int(boom['second_number']),
                      summa=summa,
                      minus=minus,
                      division=division,
                      multiply=multiply,
                      )
        obj_db.save()
        return render(request, 'calculate.html',
                      {"response0": summa, "response1": minus, "response2": multiply,
                       "response3": division, "responsefirst": first_number, "responsesecond": second_number,
                       'list_calculate': list})


    else:
        empty = " Введите \"Первое число\" + \"Второе число\" "
        return render(request, 'calculate.html', {"list_calculate": list, "response00": empty})