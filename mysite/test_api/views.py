from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import AipuAccount

def get_user_address(request):
    response = {
            'id': 1,
            'content': 'come on!',
            'location': 'Taipei',
            'likes': 193,
            'address': '1K4PamQz5xgsH8VHU8DXYpDTNExzev2RTx'
            }
    status = 200
    return JsonResponse(responsr)

def get_wallet_user_by_aipuid(request, aipu_id):
    response = {}
    aipuid_list = AipuAccount.objects.all()
    for x in xrange(0, len(aipuid_list)):
        if aipuid_list[x].aipu_id == aipu_id:
            

