from django.shortcuts import render
from login.models import Login
from django.contrib import messages
# Create your views here
def log(request):
     if request.method == "POST":
          unm = request.POST.get('user')
          pwd = request.POST.get('auth_pass')

          print(unm)
          print(pwd)

          obj = Login.objects.filter(username=unm, password=pwd)
          for x in obj:
               ty = x.type
               u_id = x.u_id

               if ty == 'authority':
                    request.session['uid'] = u_id
                    return render(request, 'temp/authority_home.html')
          messages.info(request,"incorrect ")
               # elif ty == 'manager':
               #      request.session['uid'] = u_id
               #      return render(request, 'temp/manager_home.html')
               # elif ty == 'user':
               #      request.session['uid'] = u_id
               #      return render(request, 'temp/aidteam_home.html')
     return render(request,'login/login.html')


from django.http import HttpResponse
from rest_framework.views import APIView, Response
from login.serializer import android
import datetime
from login.models import Login


class log_view(APIView):
     def get(self, request):
          ob = Login.objects.all()
          ser = android(ob, many=True)
          return Response(ser.data)

     def post(self, request):
          unm = request.data['username']
          pwd = request.data['password']
          ob = Login.objects.filter(username=unm, password=pwd)

          ser = android(ob, many=True)
          return Response(ser.data)

