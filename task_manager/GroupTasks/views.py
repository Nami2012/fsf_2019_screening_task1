from django.shortcuts import render,HttpResponse

# Create your views here.
def work(request):
    return HttpResponse("<h2> heyya Group tasks is working <h2>")