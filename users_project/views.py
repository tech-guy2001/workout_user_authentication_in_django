
from django.http import HttpResponse


def home(request):
    return HttpResponse("hello i am running ..ok")



def about(request):
    return HttpResponse("about is running ..ok")


