from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def showTest(request):

    que = "Who developed c Language ?"
    a = "Himanshu"
    b = "Ghanshu"
    c = "Antoni"
    d = "Danish"
    level = 'Easy'
    data = {'que':que,'a':a,'b':b,'c':c,'d':d,'level':level}
    res = render(request,'exam/test.html',context=data)  # here exam is --> the file which is inside of templates folder, and templates folder directory is mentioned in settings.py file
    # render takes atleast three arguments , therefore 1st line is for render importing
    return res
    #s='<h1>This is show Test Page</h1>'
    #return HttpResponse(s)
def showResult(request):
    s='<h1>This is show Test Result</h1>'
    return HttpResponse(s)