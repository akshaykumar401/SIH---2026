from django.shortcuts import render, redirect
from .forms import UserProfileForm
from .models import User_Profile
from django.contrib.auth import login

# Create your views here.
def register(request):
  if request.user.is_authenticated:
    return redirect('student_dashboard')

  if request.method == 'POST':
    form = UserProfileForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.set_password(form.cleaned_data['password1'])
      user.save()
      User_Profile.objects.create(
        user=user,
        full_name=form.cleaned_data['full_name'],
        image=form.cleaned_data['image'],
        role=form.cleaned_data['role'],
      )
      # Login the user
      login(request, user)
      if user.role == "student":
        return redirect('student_dashboard')
      elif user.role == "faculty":
        return redirect('faculty_dashboard')
      elif user.role == "industry":
        return redirect('industry_dashboard')
      elif user.role == "institute":
        return redirect('institute_dashboard')
      return redirect('home')
  else:
    form = UserProfileForm()

  return render(request, 'registration/register.html', {
    'form': form,
  })