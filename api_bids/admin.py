from django.contrib import admin
from .models import Category, Auction, Watchlist, Bid, Comment

# Register your models here.

admin.site.register(Category)
admin.site.register(Auction)
admin.site.register(Watchlist)
admin.site.register(Bid)
admin.site.register(Comment)