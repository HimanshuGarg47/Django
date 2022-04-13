from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.views import View
from .forms import ReviewForm , ContactForm
from .models import Review

# Create your views here.

class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, "reviews/review.html", {"form": form})
    
    
    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            # review = Review(user_name = form.cleaned_data['user_name'],
            #                 review_text = form.cleaned_data['review_text'],
            #                 rating = form.cleaned_data['rating'])   # if we are using ModelForm we can skip this step
            form.save()
            return HttpResponseRedirect("/thank-page")
        
        
        return render(request, "reviews/review.html", {"form": form})

        
        
        
# def review(request):
#     if request.method == "POST":
#         # existing_data = Review.objects.get(pk = 1) #for updating data
#         # form = ReviewForm(request.POST, instance=existing_data)
        
        
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             # review = Review(user_name = form.cleaned_data['user_name'],
#             #                 review_text = form.cleaned_data['review_text'],
#             #                 rating = form.cleaned_data['rating'])   # if we are using ModelForm we can skip this step
#             form.save()
#             return HttpResponseRedirect("/thank-page")
#     else:
#       form = ReviewForm()
#     return render(request, "reviews/review.html", {"form": form})
#     # return render(request, "reviews/review.html", {"has_error": False})



def thanks(request):
    return render(request, "reviews/thanku_page.html")
