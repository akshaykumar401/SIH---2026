import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SkillBridge.settings")
django.setup()

from django.test import Client
from django.contrib.auth.models import User
from user.models import User_Profile

c = Client()
# create a temporary superuser
User.objects.filter(username='testadmin').delete()
su = User.objects.create_superuser('testadmin', 'admin@example.com', 'password')
c.login(username='testadmin', password='password')

response = c.get('/admin/user/user_profile/')
if response.status_code != 200:
    print(f"Error fetching list view: {response.status_code}")
    print(response.content.decode('utf-8'))
else:
    print("List view OK")
    
# test change view
up = User_Profile.objects.first()
if up:
    response = c.get(f'/admin/user/user_profile/{up.pk}/change/')
    if response.status_code != 200:
        print(f"Error fetching change view: {response.status_code}")
        print(response.content.decode('utf-8'))
    else:
        print("Change view OK")

