from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Create your models here.

class Profile(models.Model):
    sexes = (('Femme', 'Femme'), ('Homme', 'Homme'))
    types = (('Adminitrator', 'Administrator'), ('Owner', 'Owner'),  ('User', 'User'))
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    sexe = models.CharField(choices=sexes , max_length=200)
    localisation = models.CharField(max_length=200)
    typ = models.CharField(choices=types, max_length=200)
    phone = models.CharField(max_length = 10, null=True)

    def __str__(self):
        return self.user.username

class Listing(models.Model):
    statuss = (('Available', 'Available'), ('Booked', 'Booked'))
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    square_footage = models.IntegerField()
    address = models.CharField(max_length=200)
    image = models.ImageField(upload_to="pictures", null=True)
    status = models.CharField(choices=statuss, max_length=200, null=True, default="Available")
    owner = models.ForeignKey(Profile, related_name="listings", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
    
    

    
class Category(models.Model):
    name = models.CharField(max_length=200, default="Default")
    listings = models.ManyToManyField(Listing, related_name='categories', blank=True)
    
    def __str__(self):
        return self.name


class Booking(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bookings")
    price = models.IntegerField(default=0)
    start_date = models.DateField()
    end_date = models.DateField()
    
    
    def  __str__(self):
        return self.listing.title + ' for '+  str(self.price) + ', '+ str(self.start_date)
