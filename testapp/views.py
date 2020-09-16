from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import Employee
# Create your views here.

def employee_info_view(request):
     employees = Employee.objects.all() # objects are the recordes in the table , all() --> return all the record 
     data = {'employees':employees}
     res = render(request, 'testapp/employees.html',data)
     return res
     
def greeting(request):   
     # request in brackets is --> it receives request (user's request)
     # url mapped info goes i.e. httprequest goes to this function and it receives the request info. 
    s = '<h1>Hello and welcome to first view of testapp</h1><p>This is landing page</p>'

    return HttpResponse(s)

def showContact(request):
     s='<h1>Contact page</h1>'
     s+='<p>Mobile: 8920434322</p>'
     s+='<p>Emial: Somehting@gmial.com</p>'
     return HttpResponse(s)
def about(request):

     test = "this is an about page"


     # msg = "this is an about page"
     # list = [10,20,30]
     # x = 12
     return render(request,'testapp/about.html',{'test':test})
     # return render(request,'testapp/about.html',{'msg':msg,'li':list,'x':x})
     #s= '<h1>This is an about page</h1>'
     #return HttpResponse(s)