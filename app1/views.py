from django.shortcuts import render

# Create your views here.
def syed(request):
    d1={'a':10}
    return render(request,'syed.html',context=d1)
def jinjatags(request):
    d2={'b':20}
    return render(request,'jinjatags.html',context=d2)