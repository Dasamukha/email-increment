from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def email(request):
    return render(request,'email_generator/email.html')

def generated_email(request):
    st = int(request.GET.get('start'))
    ed = int(request.GET.get('end'))
    ed =ed + 1
    fname = str(request.GET.get('fname'))
    lname = '@gmail.com'
    list1 = []
    for x in range(st, ed):
        v = (fname + "+" + str(x) + lname)
        list1.append(v)
    return render(request,'email_generator/generated_email.html', {'generated':list1})