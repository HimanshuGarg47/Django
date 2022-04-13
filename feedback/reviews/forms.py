from django import forms
from .models import Review
# class ReviewForm(forms.Form):
    # user_name = forms.CharField(label="Your Name",max_length=100, error_messages={
    #     "required":"Your name must not be empty!",
    #     "max_length":"Please enter a shorter name"
    # })
    
    # review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200)
    # rating = forms.IntegerField(label="Your rating", min_value=1 , max_value=5)
    
    
    
    #basically used for directly connect/import model fields into Form 
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
                # //we can explicitly tell which fields to include
        
        fields = '__all__'      # fields = ['user_name','review_text','rating']
            #exclude specified fields
        # exclude = ['owner_comment']
        labels = {
            "user_name" : "Your Name",
            "review_text": "Your Feedback",
            "rating":"Your Rating"
        }
    
        error_messages = {
            "user_name":{
                "required":"Your name must not be empty!",
                "max_length": "Please enter a shorter name"
                
            }
        }
    
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

    # user_name.clean(' ')      # run in terminal
# from django import forms
# class CommentForm(forms.Form):
#     name = forms.CharField(label='Your name')
#     url = forms.URLField(label='Your website', required=False)
#     comment = forms.CharField()
# f = CommentForm(auto_id=False)
# print(f)