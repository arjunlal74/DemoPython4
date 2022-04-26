
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, People


def demo(request):
    obj1 = Place.objects.all()
    obj2 = People.objects.all()
    return render(request, 'index.html', {'result1':obj1,  'result2':obj2})










# def addition(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     add = x+y
#     sub = x-y
#     pro = x*y
#     div = x/y
#     return render(request, 'addition.html', {"add": add, "sub": sub, "pro": pro, "div": div})

# def about(request):
#     return render(request, 'about.html')
#
# def contact(request):
#     return render(request,  'contact.html')
#
# def details(request):
#     return render(request,  'details.html')
#
# def thanks(request):
#     return render(request,  'thanks.html')