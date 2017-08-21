from django import forms
from .models import Post, Author, Category, Comnt


from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)

# User = get_user_model()

# from .models import Cmnt

# class CommentForm(forms.ModelForm):
# 	class Meta:
# 		model = Cmnt
# 		fields = ('author', 'body', 'date') 


# class CommentForm(forms.ModelForm):
# class CommentForm(forms.Form):
# 	content = forms.CharField(label = 'Comment here')
# 	author = forms.CharField(label = 'Your Name')
# 	comnt_on = forms.CharField(label = 'Blog Title')

# 	class Meta:
# 		model = Comnt
# 		fields = [
# 			'content',
# 			'author',
# 			# 'email2'
# 			'comnt_on'
# 		]
# 		# widgets = {
#   #           'content': textarea(attrs={'cols': 80, 'rows': 20}),
#   #       }
# 	def clean(self, *args, **kwargs):
# 		author = self.cleaned_data.get("author")
# 		if author :

# 			return super(CommentForm, self).clean(*args, **kwargs)



class CommentCreateForm(forms.Form):
	content			= forms.CharField(label = 'Comment here')
	author 			= forms.CharField(label = 'Your Name', required= False)
	comnt_on		= forms.CharField(label = 'Blog Title', required= False)

	def clean_content(self):
		content = self.cleaned_data.get("content")
		return content


class CommentNewCreateForm(forms.ModelForm):
	class Meta:
		model = Comnt
		fields = [
			'content',
			'author',
			'comnt_on',
		]


	# def clean_email2(self):
	# 	email = self.cleaned_data.get('email')
	# 	email2 = self.cleaned_data.get('email2')
	# 	if email != email2:
	# 		raise forms.ValidationError("Emails must match")
	# 	email_qs = User.objects.filter(email=email)
	# 	if email_qs.exists():
	# 		raise forms.ValidationError("This email has already been registered")
	# 	return email	