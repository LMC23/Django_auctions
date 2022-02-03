from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title

class Auction(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500, validators=[MinLengthValidator(10, message='Please enter at least 10 characters.')])
    starting_price = models.DecimalField(max_digits=19, decimal_places=2)
    currency = models.CharField(max_length=3, default='EUR')
    url = models.CharField(max_length=250, blank=True, null=True)

    #ForeignKeys
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Watchlist(models.Model):

    #ForeignKeys
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.user} - {self.auction}'

class Bid(models.Model):
    bid = models.DecimalField(max_digits=19, decimal_places=2)

    #ForeignKeys
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.user} bid {self.bid} {self.auction.currency} for {self.auction}'

class Comment(models.Model):
    content = models.CharField(max_length=4000)

    #ForeignKeys
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    auction = models.ForeignKey(Auction, on_delete=models.SET_NULL, blank=True, null=True, related_name="comments")

    def __str__(self):
        return f'{self.user} commented on {self.auction}'



# user = User.getbyid(iduser)

# comments = Comment.getbyuserid(iduser)

# comments = User.comments.all()