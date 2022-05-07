from django.shortcuts import render

# Create your views here.
from reminder.models import Remainder
from django.http import HttpResponse
from rest_framework.views import APIView,Response
from reminder.serializer import android
import datetime
class rem(APIView):
    def get(self,request):
        ob=Remainder.objects.all()
        ser=android(ob,many=True)
        return Response(ser.data)
    def post(self,request):
        ob = Remainder()
        ob.title = request.data['title']
        ob.date = request.data['date']
        ob.time=request.data['time']


        ob.alert_mode=request.data['alert_mode']
        ob.save()

        return HttpResponse('POST')

class editrem(APIView):
    def post(self,request):
        v=request.data['remainder_id']
        ob=Remainder.objects.get(remainder_id=v)
        # ob.title = request.data['title']
        ob.date = request.data['date']
        ob.time=request.data['time']
        ob.save()
        return HttpResponse('POST')

class deleterem(APIView):
    def post(self,request):
        v=request.data['rid']
        ob = Remainder.objects.get(remainder_id=v).delete()

        return HttpResponse('POST')
