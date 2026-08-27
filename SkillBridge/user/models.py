from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
import cloudinary.uploader

# Create your models here.
class User_Profile(models.Model):
    # Enum for role
    ROLE = [
        ('student', 'Student'),
        ('faculty', 'Faculty'),
        ('industry', 'Industry'),
        ('institute', 'Institute'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    full_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100,choices=ROLE,default='student')
    image = CloudinaryField('image', folder='SkillBridge/avatars/', blank=True, null=True)
    
    def __str__(self):
        return self.full_name

@receiver(pre_save, sender=User_Profile)
def delete_old_image_on_change(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_profile = User_Profile.objects.get(pk=instance.pk)
            if old_profile.image and old_profile.image != instance.image:
                cloudinary.uploader.destroy(old_profile.image.public_id)
        except User_Profile.DoesNotExist:
            pass

@receiver(post_delete, sender=User_Profile)
def delete_image_on_delete(sender, instance, **kwargs):
    if instance.image:
        cloudinary.uploader.destroy(instance.image.public_id)
