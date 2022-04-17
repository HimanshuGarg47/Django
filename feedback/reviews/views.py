from email.mime import base
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views import View
from .forms import ReviewForm
from .models import Review

# Create your views here.

class ReviewView(FormView):
    form_class = ReviewForm
    template_name = 'reviews/review.html'
    success_url = '/thank-page'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    # def get(self, request):   #View class is inherited instead of FormView
    #     form = ReviewForm()
    #     return render(request, "reviews/review.html", {"form": form})
    
    
    # def post(self, request):
    #     form = ReviewForm(request.POST)
    #     if form.is_valid():
    #         # review = Review(user_name = form.cleaned_data['user_name'],
    #         #                 review_text = form.cleaned_data['review_text'],
    #         #                 rating = form.cleaned_data['rating'])   # if we are using ModelForm we can skip this step
    #         form.save()
    #         return HttpResponseRedirect("/thank-page")
        
        
    #     return render(request, "reviews/review.html", {"form": form})

    
class ThankView(TemplateView):
    template_name = "reviews/thanku_page.html"
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "This works"
        return context
           
        
class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"
    
class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review  
    
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get("favorite_view")
        context["is_favorite"] = favorite_id == str(loaded_review.id)
        return context
        
class AddFavoriteView(View):
    def post(self,request):
        review_id = request.POST["review_id"]
        request.session["favorite_view"] = review_id
        # fav_view = Review.objects.get(pk = review_id)
        # request.session['favorite_view'] = fav_view  # this is wrong bcz we are storing object in session
        return HttpResponseRedirect("/reviews/" + review_id)

        
    # def get_queryset(self):
    #    base_query = super().get_queryset()
    #    data = base_query.filter(rating__gt=4)
    #    return data
       
    
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     reviews = Review.objects.all()
    #     context["reviews"] = reviews
    #     return context

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     review_id = kwargs["id"]
        
    #     singlereview = Review.objects.get(pk=review_id)
    #     context["review"] = singlereview
    #     return context
     
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



