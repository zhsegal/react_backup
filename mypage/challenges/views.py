import re
from django.shortcuts import render


def index (request):
    return render(request,'challenges/index.html')