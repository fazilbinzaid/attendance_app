from django import forms


class LoginForm(forms.Form):
	username = forms.CharField(max_length=32)
	password = forms.CharField(max_length=32)


class UserForm(forms.Form):
	username = forms.CharField(max_length=32)
	password = forms.CharField(widget=forms.PasswordInput)
	confirm_password = forms.CharField(max_length=32)
	name = forms.CharField(max_length=32)
	email = forms.EmailField()

	def __init__(self, *args, **kwargs):
		super(UserForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs.update({'class': 'form-control',
									  'placeholder': field})

	def clean(self):
		cleaned_data = super(UserForm, self).clean()
		password = cleaned_data.get('password')
		confirm_password = cleaned_data.pop('confirm_password')
		if not password == confirm_password:
			raise forms.ValidationError("passwords donot match. Please re-enter.")
		print(cleaned_data)
		return cleaned_data