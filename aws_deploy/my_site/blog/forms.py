from django import forms
from .models import Posts,Author,Tag , Comment

class CreatePost(forms.ModelForm):
   
    class Meta:
        
        model = Posts
        fields = '__all__'
        
        
        # labels = {
        #     "content" : "Post Content",
            
           
        #     "image":"Upload your post image here"
        # }
        # field_classes = {
        #     'tagline': forms.MultipleChoiceField(queryset=Tag.objects.all(),widget=forms.CheckboxSelectMultiple),
        # }
        
        exclude = ['slug']
    tagline = forms.MultipleChoiceField(choices=Tag.objects.values_list('id', 'caption'),widget=forms.CheckboxSelectMultiple)
    author = forms.ModelChoiceField(queryset=Author.objects.all(),required=True)
        
    
        # error_messages = {
        #     "user_name":{
        #         "required":"Your name must not be empty!",
        #         "max_length": "Please enter a shorter name"
                
        #     }
        # }
        
class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']
        labels = {
            "user_name":"Your Name",
            "user_email" : "Your Email Id",
        }