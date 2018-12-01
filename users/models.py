from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User

CATEGORIES = (
    ('SF', 'Science fiction'), ('FA', 'Fantasy'), ('DR', 'Drama'),
    ('CO', 'Comedy'), ('HI', 'Historical'), ('RO', 'Romance'), ('AC', 'Action'),
    ('TR', 'Travel'), ('MY', 'Mystery'), ('AD', 'Adventure'), ('TH', 'Thriller')
)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    place_of_live = models.CharField(max_length=50, null=True, blank=True)
    education = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=50,null=True, blank=True)
    about_be = models.TextField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    favorite_categories = MultiSelectField(max_length=50, null=True, blank=True, choices=CATEGORIES)
    favorite_writers = models.CharField(max_length=50, null=True, blank=True)
    user_image = models.ImageField(default="default-user-image.png", upload_to='pic')

    def __str__(self):
        return self.email



# class UserProfile_2(models.Model):
#
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     user_image = models.ImageField(default="default-user-image.png", upload_to='pic')
#
#     def __str__(self):
#         return self.email