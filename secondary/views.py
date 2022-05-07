from django.shortcuts import render

# Create your views here.

from secondary.models import SecondaryUser
from django.http import HttpResponse
from rest_framework.views import APIView,Response
from secondary.serializer import android
import datetime
class secuser(APIView):
    def get(self,request):
        ob=SecondaryUser.objects.all()
        ser=android(ob,many=True)
        return Response(ser.data)
    def post(self,request):
        ob = SecondaryUser()
        ob.user_name = request.data['user_name']
        ob.address = request.data['address']
        ob.phone_no=request.data['phone_no']
        ob.user_id = "1"


        ob.date=datetime.datetime.today()
        ob.status='paid'
        ob.save()
        # obj = Carttable.objects.filter(cart_id=request.data['cart_id'])
        #
        # obj.status = 'paid'
        # # obj.date = datetime.datetime.today()
        # obj.save()
        return HttpResponse('POST')

