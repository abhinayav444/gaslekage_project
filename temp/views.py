from django.shortcuts import render

# Create your views here.

def mainhome(requset):
    return render(requset,'temp/mainhome.html')



def authority_home(requset):
    return render(requset,'temp/authority_home.html')