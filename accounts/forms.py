from django import forms
from accounts.models import Student, Teacher

CHOICES = (0, 1)

class LoginForm(forms.Form):
	username = forms.CharField(max_length=32)
	password = forms.CharField(max_length=32)


class UserForm(forms.Form):
	username = forms.CharField(max_length=32)
	password = forms.CharField(widget=forms.PasswordInput)
	confirm_password = forms.CharField(max_length=32)
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
		return cleaned_data

class StudentForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(StudentForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs.update({'class': 'form-control'})

	class Meta:
		model = Student
		fields = ('batch', 'full_name', 'roll_no',
				  'register_no', 'guardian_name', 'contact_no',
				  'address')

class TeacherForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(StudentForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs.update({'class': 'form-control'})

	class Meta:
		model = Teacher
		fields = ('first_name', 'last_name', 'guardian_name',
				  'contact_no', 'address')
