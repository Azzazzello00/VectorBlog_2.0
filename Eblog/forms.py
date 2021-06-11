from django import forms
from .models import Post, Category

#choices = [('Eletrronica', 'Eletrronica'), ('Mecanica', 'Mecanica'), ('Mecatronica', 'Mecatronica')]

choices = Category.objects.all().values_list('name', 'name')
#tags = Post.objects.all().values_list('title_tag', 'title_tag')

choices_list = []
#tags_list = []

for item in choices:
	choices_list.append(item)
#for item in tags:
	#tags_list.append(item)

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'title_tag', 'category', 'author', 'body', 'snippet', 'header_image')

		widgets = {
			'title' : forms.TextInput(attrs={'class': 'form-control'}),
			'title_tag' : forms.TextInput( attrs={'class': 'form-control', }),
			'category' : forms.Select(choices=choices_list, attrs={'class': 'form-control'}),
			#'author' : forms.Select(attrs={'class': 'form-control'}),
			'author' : forms.TextInput( attrs={'class': 'form-control', 'value' : '', 'id' : 'Victor',  'type':'hidden'}),
			'body' : forms.Textarea(attrs={'class': 'form-control'}),
			'snippet' : forms.Textarea(attrs={'class': 'form-control'}),
					}


class EditForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'title_tag', 'body', 'snippet', 'header_image')


		widgets = {
			'title' : forms.TextInput(attrs={'class': 'form-control'}),
			'title_tag' : forms.TextInput(attrs={'class': 'form-control'}),
			#'author' : forms.TextInput(attrs={'class': 'form-control'}),
			'body' : forms.Textarea(attrs={'class': 'form-control'}),
			'snippet' : forms.Textarea(attrs={'class': 'form-control'}),

		}