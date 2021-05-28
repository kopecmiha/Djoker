from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .models import User
import json

def hello(request):
    user_list = str({"hello": "world"})
    user_list = json.loads(user_list)
    return JsonResponse({"result": user_list})

def users(request):
    #user_list = str(list(User.objects.all())).replace("'", '"')
    user_list = [json.loads(str(obj.__str__()).replace("\'", "\"")) for obj in list(User.objects.all())]
    #user_list = json.dumps(user_list)
    return JsonResponse({"result": user_list})

@csrf_exempt
def write_user(request):
    if request.method == "POST":
        request = json.loads(request.body)
        name = request['name']
        last_name = request['last_name']
        patronimyc = request['patronimyc']
        type = request['type']
        organization = request['organization']
        avatar_image = request['avatar_image']
        email = request['email']
        password = request['password']
        r = User(name=str(name),
                 last_name=str(last_name),
                 patronimyc=str(patronimyc),
                 type=str(type),
                 email=str(email),
                 password=str(password),
                 organization=str(organization),
                 avatar_image=str(avatar_image),
                 )
        r.save()
        return JsonResponse({"Response": r.__str__()})
    else:
        return HttpResponse(status=405)

@csrf_exempt
def delete_user(request):
    if request.method == "POST":
        request = json.loads(request.body)
        user_id = request['id']
        User.objects.filter(id=user_id).delete()
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=405)

@csrf_exempt
def delete_all(request):
    if request.method == "GET":
        for i in User.objects.all():
            i.delete()
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=405)

@csrf_exempt
def update_user(request):
    if request.method == "POST":
        request = json.loads(request.body)
        user_id = request['id']
        dictionary = request.POST.dict()
        User.objects.filter(id=user_id).update(**dictionary)
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=405)