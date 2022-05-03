from msilib.schema import ListView
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Posts
from django.views.generic.edit import FormView
from django.views.generic import ListView 
from django.views import View
from django.views.generic.base import TemplateView
from .forms import CreatePost , CommentsForm
    
    

def get_date(post):
    return post.pub_date


class StartingPageView(ListView):
    template_name = 'blog/index.html'
    model = Posts
    ordering = ["-pub_date"]
    context_object_name = "posts"
    
    
    def  get_queryset(self):
        query =  super().get_queryset()
        data = query[:3]
        return data
    
# def starting_page(request):
#     postsi = Posts.objects.all().order_by('pub_date')[:3]
    
#     # sorted_posts = sorted(postsi,key=postsi)
#     # latest_posts = sorted_posts[-3:]
#     # latest_posts = postsi[-3:]

#     return render(request,"blog/index.html", {
#         "posts":postsi
#     })

class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Posts
    ordering = ["-pub_date"]
    context_object_name = "all_posts"
    
# def posts(request):
    
#     return render(request, "blog/all-posts.html",{
#         "all_posts":Posts.objects.all()
#     })



class CreateNewPage(FormView):
    form_class = CreatePost
    template_name = 'blog/createpost.html'
    success_url = '/thank-page'
    
    def form_valid(self, form):
        form.save()
        form = CreatePost
        return super().form_valid(form)
    
    
    
class ThankView(TemplateView):
    template_name = "blog/thank-page.html"
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Your new post created successfully!"
        return context
    
    
class  SinglePostView(View):      #class  SinglePostView(DetailView):
    
    # template_name = "blog/post-detail.html"
    # model = Posts
    # context_object_name = "post"
    
    def is_saved_post(self,request,post_id):
        saved_posts = request.session.get("stored_posts")

        if saved_posts is not None:
            is_saved_later = post_id  in saved_posts
        else:
            is_saved_later = False
            
        return is_saved_later
    
    
    def get(self , request, slug):
        post = Posts.objects.get(slug=slug)
        
        
        
        context={
            "post":post,
            "post_tags":post.tagline.all(),
            "comment_form":CommentsForm(),
            "comments":post.comments.all().order_by("-id"),
            "is_saved_later": self.is_saved_post(request,post.id),
            
        }
        return render(request, "blog/post-detail.html", context)


    def post(self,request, slug):
        comment_form = CommentsForm(request.POST)
        post = Posts.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)    # not hit database
            comment.post = post          # adding post field to form
            comment.save()              # hit database
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))
        
        context={
            "post":post,
            "post_tags":post.tagline.all(),
            "comment_form":comment_form,
            "comments":post.comments.all().order_by("-id"),
            "is_saved_later": self.is_saved_post(request,post.id),
        }
        return render(request, "blog/post-detail.html", context)
        

class ReadLaterView(View):
    
    def get(self, request):
        stored_posts = request.session.get("stored_posts")
        context = {}
        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Posts.objects.filter(id__in =stored_posts)
            context["posts"] = posts
            context["has_posts"] = True
        
        return render(request, "blog/stored-posts.html", context)
    
            
            
            
        
        
        
        
        
    def post(self,request):
        stored_posts = request.session.get("stored_posts")
        
        if stored_posts is None:
            stored_posts = []
            
            
        post_id = int(request.POST["post_id"])
        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)
        
            
        request.session["stored_posts"] = stored_posts
        return HttpResponseRedirect('/')
            
    # def get_context_data(self, **kwargs):
    #     context =  super().get_context_data(**kwargs)
    #     context['comment_form'] = CommentsForm()
    #     context['post_tags'] = self.object.tagline.all()
    #     return context
    
    
    
    
    
# def post_detail(request , slug):
#     post = Posts.objects.get(slug=slug)
    
#     # post_det = {}
#     # for post in all_posts:
#     #     if post['slug'] == slug:
#     #         post_det = post
#     #if post:
#     return render(request, "blog/post-detail.html", {
#         "post":post
#          })
    
    
    
    
    
    
    
# Create your views here.
# all_posts = [
#     {
#         "slug": "hike-in-the-mountains",
#         "image": "mountains.jpg",
#         "email":"himan@gmail.com",
#         "author": "Maximilian",
#         "date": date(2021, 7, 21),
#         "title": "Mountain Hiking",
#         "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
#         "content": """
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#         """
#     },
#     {
#         "slug": "programming-is-fun",
#         "image": "coding.jpg",
#         "email":"himan@gmail.com",
#         "author": "Maximilian",
#         "date": date(2022, 3, 10),
#         "title": "Programming Is Great!",
#         "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
#         "content": """
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#         """
#     },
#     {
#         "slug": "into-the-woods",
#         "image": "woods.jpg",
#         "email":"himan@gmail.com",

#         "author": "Maximilian",
#         "date": date(2020, 8, 5),
#         "title": "Nature At Its Best",
#         "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
#         "content": """
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#          uis architecto ipsam nemo. Odio.
#         """
#     },
#     {
#         "slug": "Hack-the-mind",
#         "image": "woods.jpg",
#         "email":"himan@gmail.com",
#         "author": "Himanshu",
#         "date": date(2022, 8, 5),
#         "title": "Mind is never secure",
#         "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
#         "content": """
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#         """
#     }
# ]

# for post in all_posts:
    
    
#     if not Posts.objects.filter(title=post['title']):
#         authorp = Author(first_name=post['author'],email=post['email'])
#         authorp.save()
#         tags = Tag.objects.create(caption="django")
#         tags.save()
#         posti = Posts(slug=post['slug'],title=post['title'],excerpt=post['excerpt'],image_name=post['image'],author = authorp,content = post['content'])
#         posti.save()
#         postp = Posts.objects.get(title=post['title'])
#         postp.tagline.add(tags)
#         postp.save()