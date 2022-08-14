from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt

from .models import User


@csrf_exempt
def checkUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        mac_adress = request.POST.get('mac_adress')

        user_obj = User.objects.filter(name=username, password=password)
        if user_obj.exists():
            user = user_obj[0]
            print(user.mac)
            if user.mac == '0':
                user.mac = mac_adress
                user.save()
                return JsonResponse(data={'auth': True, 'active': user.active, 'message': "login success"})
            else:
                addr_match = mac_adress == user.mac
                if not addr_match:
                    return JsonResponse(data={'auth': False, 'active': user.active, 'message': "Unabled to login this device"})
                return JsonResponse(data={'auth': True, 'active': user.active, 'message': "login success"})
        return JsonResponse(data={'auth': False, 'message': "user name and password doesn't match"})
