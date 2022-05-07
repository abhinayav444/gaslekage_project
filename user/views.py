from django.shortcuts import render

# Create your views here.

from secondary.models import SecondaryUser
from django.http import HttpResponse
from rest_framework.views import APIView,Response
from user.serializer import android
import datetime
from user.models import User
from user.serializer import android1
from user.serializer import android
from user.models import AddLocation
from login.models import Login

class user(APIView):
    def get(self,request):
        ob=User.objects.all()
        ser=android(ob,many=True)
        return Response(ser.data)
    def post(self,request):
        ob=User()
        ob.user_name=request.data['username']
        # ob.user_name = request.data['user_name']
        ob.address=request.data['address']
        ob.post_office = request.data['post_office']
        ob.pincode = request.data['pincode']
        ob.district = request.data['district']
        ob.email_id = request.data['email_id']
        ob.gender = request.data['gender']

        ob.date=datetime.datetime.today()
        ob.status='paid'
        ob.save()
        obj =Login()
        obj.u_id = ob.user_id
        obj.username = request.data['username']
        obj.password = request.data['password']
        obj.type = "user"



        obj.save()
        return HttpResponse('POST')


class user_addloc(APIView):
    def get(self,request):
        ob=AddLocation.objects.all()
        ser=android1(ob,many=True)
        return Response(ser.data)
    def post(self,request):
        ob=AddLocation()
        # ob.location_id=request.data['location_id']
        ob.state=request.data['state']
        #ob.location = request.data['location']
        ob.latitude = request.data['latitude']
        ob.longitude = request.data['longitude']
        ob.user_id = request.data['user_id']
        ob.save()

        return HttpResponse('POST')
