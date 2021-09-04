import random
from django.shortcuts import render

# Create your views here.


def lotto_index(req):
    lotto_number = random.sample(range(1, 46), 7)
    context = {
        'lotto_number': lotto_number,
    }
    return render(req, 'lotto.html', context)


def calculator_index(req):
    formula = req.GET.get('formula')

    if formula:
        result = eval(formula)
    else:
        result = None

    context = {
        'result': result
    }
    return render(req, 'calculator.html', context)
