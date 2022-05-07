from django.shortcuts import render
from authority.models import Authourity
from login.models import Login
from user.models import User
from secondary.models import SecondaryUser
# Create your views here.
def info(request):
    obb=SecondaryUser.objects.all()
    context={
        'obbval':obb,
    }

    return render(request,'authority/contactinfo.html',context)



def reg(request):
    if request.method=="POST":
        obj=Authourity()
        obj.branch_name=request.POST.get('branch_name')
        obj.branch_loc=request.POST.get('branch_loc')
        obj.email=request.POST.get('authority_mail')
        obj.password=request.POST.get('authority_password')
        obj.helpline_no=request.POST.get('helpline_no')
        obj.save()

        obb=Login()
        obb.username=request.POST.get('authority_mail')
        obb.password=request.POST.get('authority_password')
        obb.type='authority'
        obb.u_id=obj.branch_id
        obb.save()
    return render(request,'authority/reg.html')