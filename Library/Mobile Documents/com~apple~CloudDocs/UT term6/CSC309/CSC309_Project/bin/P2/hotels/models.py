from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
# from django.contrib.auth.models import User
# import sys
# sys.path.append('bin/P2/')
# from accounts.models import MyUser
import sys
sys.path.append('..')
import accounts

# Create your models here.

# def default_available_date():
#     return date.today() + timedelta(days=30)

# content_type=ContentType.objects.get_for_model(Hotel)
# two types of comment, one from guest to property, another from host to guest
class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    detail = models.CharField(max_length=1000)
    author = models.ForeignKey(accounts.models.MyUser, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.detail}"


class Hotel(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    owner = models.ForeignKey(accounts.models.MyUser, on_delete=models.SET_NULL, related_name='owner', null=True)
    address = models.CharField(max_length=200)
    rating = models.DecimalField(max_digits=2, decimal_places=1,
                                 validators=[MinValueValidator(0), MaxValueValidator(5)])
    capacity = models.IntegerField(validators=[MinValueValidator(0)])
    beds = models.IntegerField(validators=[MinValueValidator(0)])
    baths = models.IntegerField(validators=[MinValueValidator(0)])
    is_active = models.BooleanField(default=True)
    comments = GenericRelation(Comment, related_query_name='hotels')

    def __str__(self):
        return f"{self.name}"


class HotelAvailability(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(decimal_places=2, validators=[MinValueValidator(0)], max_digits=1000)

    def __str__(self):
        return f"{self.hotel} available from {self.start_date} to {self.end_date}"


# Pending: the user makes a request to reserve a property on one or more consecutive dates.
# Denied: the host, i.e., the owner of the property, declines the reservation request.
# Expired: the host did not respond to a reservation request within a user-defined time window.
# Approved: the reservation request is approved.
# Canceled: the reservation was approved but later canceled by the user.
# Terminated: the reservation was approved but later canceled by the host.
# Finished: the reservation is realized, i.e., the user went to the property and stayed there.
class Reservation(models.Model):
    STATUS = [
        ('A', 'Approved'),
        ('P', 'Pending'),
        ('Ca', 'Cancelled'),
        ('D', 'Denied'),
        ('E', 'Expired'),
        ('T', 'Terminated'),
        ('F', 'Finished'),
    ]
    guest = models.ForeignKey(accounts.models.MyUser, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    state = models.CharField(choices=STATUS, max_length=120)


class Notification(models.Model):
    receiver = models.ForeignKey(accounts.models.MyUser, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)
    date = models.DateTimeField(null=True, blank=True)
    message = models.TextField()

    def get_map(self):
        return {"receiver": self.receiver,
                "read": self.read,
                "date": self.date,
                "message": self.message}
