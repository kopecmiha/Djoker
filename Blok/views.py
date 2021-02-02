from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .models import User
import json

def hello(request):
    user_list = str({"hello": "world"}).replace("'", '"')
    user_list = json.loads(user_list)
    return JsonResponse({"result": user_list})

def users(request):
    user_list = str(list(User.objects.all())).replace("'", '"')
    user_list = json.loads(user_list)
    return JsonResponse({"result": user_list})

@csrf_exempt
def write_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        r = User(username = username, email = email, password = password)
        r.save()
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=405)

@csrf_exempt
def delete_user(request):
    if request.method == "POST":
        user_id = request.POST.get('id')
        User.objects.filter(id=user_id).delete()
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=405)

@csrf_exempt
def update_user(request):
    if request.method == "POST":
        user_id = request.POST.get('id')
        dictionary = request.POST.dict()
        User.objects.filter(id=user_id).update(**dictionary)
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=405)