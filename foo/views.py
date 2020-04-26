import requests
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def liveness(request):
    data = {"status": "+OK", "msg": "Liveness OK"}
    return JsonResponse(data, status=200)


def readiness(request):
    data = {"status": "+OK", "msg": "rediness OK"}
    return JsonResponse(data, status=200)


def liveness2(request):
    data = {"status": "-ERR", "msg": "Liveness error"}
    return JsonResponse(data, status=500)


def readiness2(request):
    data = {"status": "-ERR", "msg": "readiness error"}
    return JsonResponse(data, status=500)


def liveness3(request):
    URL = "http://127.0.0.1:7000/liveness"
    resp = requests.get(URL)
    if resp.status_code == 200:
        data = {"status": "+OK", "msg": "Liveness OK"}
        return JsonResponse(data, status=200)
    data = {"status": "-ERR", "msg": "Liveness error"}
    return JsonResponse(data, status=500)


def readiness3(request):
    URL = "http://127.0.0.1:7000/readiness"
    resp = requests.get(URL)
    if resp.status_code == 200:
        data = {"status": "+OK", "msg": "rediness OK"}
        return JsonResponse(data, status=200)
    data = {"status": "-ERR", "msg": "readiness error"}
    return JsonResponse(data, status=500)

