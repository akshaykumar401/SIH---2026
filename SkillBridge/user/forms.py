from django import forms
from .models import User_Profile

class UserProfileForm(forms.Form):
  # Enum for role
  ROLE = [
    ('student', 'Student'),
    ('faculty', 'Faculty'),
    ('industry', 'Industry'),
    ('institute', 'Institute'),
  ]

  email = forms.EmailField(max_length=100, required=True, label='Email')
  password = forms.CharField(max_length=100, required=True, label='Password', widget=forms.PasswordInput)
  confirm_password = forms.CharField(max_length=100, required=True, label='Confirm Password', widget=forms.PasswordInput)
  full_name = forms.CharField(max_length=100, required=True, label='Full Name')
  image = forms.ImageField(required=False)
  role = forms.CharField(max_length=100, required=True, label='Role', widget=forms.Select(choices=ROLE))
  
  class Meta:
    model = User_Profile
    fields = ['email', 'password1', 'password2', 'full_name', 'image', 'role']
