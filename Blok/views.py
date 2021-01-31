from django.shortcuts import render

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import json, time
from datetime import datetime

def hello(request):
    user_list = str({"hello": "world"}).replace("'", '"')
    user_list = json.loads(user_list)
    return JsonResponse({"result": user_list})