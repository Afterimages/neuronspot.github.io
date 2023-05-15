from django.shortcuts import render,HttpResponse
from app01.models import *

# Create your views here.

def index(request):
    return render(request,"index.html")

def result(request):
    if request.method =='GET':
        neuron_name = request.GET.get("neuron_name")
        neuron_name = neuron_name.capitalize() #转换大小写
        neuron_name= globals()[neuron_name] #将字符串转为变量
        ada = neuron_name.objects.all()

        #return HttpResponse(form)
        return render(request,"result.html",locals())