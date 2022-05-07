from django.shortcuts import render
from precautions.models import Precaution
# Create your views here.
def prec(request):
    if request.method=="POST":
        obj=Precaution()
        obj.precautions=request.POST.get('authority_add')
        obj.save()
    return render(request,'precautions/precautions_authority.html')



from precautions.models import Precaution
from django.http import HttpResponse
from rest_framework.views import APIView,Response
from precautions.serializer import android
import datetime

def preca(request):
    if request.method=="POST":
        obj=Precaution()
        obj.precautions=request.POST.get('authority_add')
        obj.save()
    return render(request,'precautions/precautions_authority.html')

class prec_view(APIView):
    def get(self,request):
        ob=Precaution.objects.all()
        ser=android(ob,many=True)
        return Response(ser.data)
    def post(self,request):
        ob = Precaution()
        ob.precautions = request.data['precautions']

        ob.date=datetime.datetime.today()
        ob.status='paid'
        ob.save()
        # obj = Carttable.objects.filter(cart_id=request.data['cart_id'])
        #
        # obj.status = 'paid'
        # # obj.date = datetime.datetime.today()
        # obj.save()
        return HttpResponse('POST')






