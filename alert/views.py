from django.shortcuts import render
from alert.models import Alert
# Create your views here.
def view(request):
    obj=Alert.objects.all()
    context={
        'objavl':obj,
    }
    return render(request,'alert/view_alert.html',context)


from django.http import HttpResponse
from rest_framework.views import APIView, Response
from alert.serializer import android
import datetime
from alert.models import Alert


class alertt(APIView):
    def get(self, request):
        ob = Alert.objects.all()
        ser = android(ob, many=True)
        return Response(ser.data)

    def post(self, request):
        ob = Alert()



        # obj = Carttable.objects.filter(cart_id=request.data['cart_id'])
        #
        # obj.status = 'paid'
        # # obj.date = datetime.datetime.today()
        # obj.save()
        return HttpResponse('POST')

class alertstatus(APIView):
    def post(self,request):
        v = request.data['alert_id']
        ob = Alert.objects.get(alert_id=v)
        ob.status = "Forwarded"
        ob.save()

        return HttpResponse('POST')
