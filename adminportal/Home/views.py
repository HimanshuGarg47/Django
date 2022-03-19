from django.shortcuts import render
from django.http import HttpResponse , Http404  , HttpResponseRedirect , HttpResponseNotFound
from django.urls import reverse
from Home.models import Student
import datetime

# from django.template.loader import render_to_string

# Create your views here.
# views are responsible for processing requests and return response
# may be implemented by function or class



def index(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return render(request,'Home/index.html',{})
     
     
     
def contact(request):
    if request.method == "POST":
        fullname = request.POST.get('name')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        message = request.POST.get('message')
        print(fullname , email , phonenumber, message)
        ins = Student(name=fullname, email=email , number = phonenumber, textbox= message)
        ins.save()

        
    return render(request,'Home/contact.html',{'email':email})

    # return HttpResponse(final_month)
    
# def monthly_challenges_by_number(request,month):
#     months = list(monthly_challenges.keys())
#     redirect_month = months[month-1]
    
#     # return HttpResponse(redirect_month)
#     redirect_path =  reverse("month_challenge",args=[redirect_month])   # challenge/january
#     return HttpResponseRedirect(redirect_path)
#     # return HttpResponseRedirect("/challenge/" + redirect_month)

# def month_challenges(request,month):
    
#     try:
#          challenge_text = monthly_challenges[month.lower()]
#          #shortcut of render_to_string and return response
#          return render(request ,"challenges/challenges.html",{
#              "text" : challenge_text,
#              "month_name":month
#          })
     
     
     
#         #  response_data = render_to_string("challenges/challenges.html")
#         #  return HttpResponse(response_data)
#     except:
#         raise Http404()
#         # response_data = render_to_string("404.html")
#         # return HttpResponseNotFound(response_data)
    
        
        
