import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

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
    resp = requests.get(settings.LIVENESS_ENDPOINT)
    if resp.status_code == 200:
        data = {"status": "+OK", "msg": "Liveness OK"}
        return JsonResponse(data, status=200)
    data = {"status": "-ERR", "msg": "Liveness error"}
    return JsonResponse(data, status=500)


def readiness3(request):
    resp = requests.get(settings.READINESS_ENDPOINT)
    if resp.status_code == 200:
        data = {"status": "+OK", "msg": "rediness OK"}
        return JsonResponse(data, status=200)
    data = {"status": "-ERR", "msg": "readiness error"}
    return JsonResponse(data, status=500)

