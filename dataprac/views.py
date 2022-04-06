from django.shortcuts import render
from django.http import HttpResponse

def homeView(req):
    my_list = [1,2,3,4,"5 is the number with string format",6.66,70,800,-99,1000]
    my_list.append([56,998])
    my_list.extend([56,998])
    return HttpResponse(my_list)
