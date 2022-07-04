from django.shortcuts import render
from django.http import JsonResponse

def apiOverview(request):
    return JsonResponse("{[API BASE]}",safe=False)
