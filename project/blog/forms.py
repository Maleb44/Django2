####
from django import forms
import datetime
from django.utils.text import slugify

class PostForm(forms.Form):
	title = forms.CharField(max_length=25)
	slug  = slugify(title)
	date  = datetime.datetime.utcnow().isoformat()
	content = forms.CharField(required=False,widget=forms.Textarea) 

