from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User model with is_premium field for Task 4
class User(AbstractUser):
    is_premium = models.BooleanField(default=False)

# Task 1: Music app Playlist model
class Playlist(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='playlists')

    def __str__(self):
        return self.name

# Task 2: Zomato-style Food Order model
class Order(models.Model):
    restaurant_name = models.CharField(max_length=100)
    item_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.item_name}"

# Task 3: Flipkart-style Shopping CartItem model
class CartItem(models.Model):
    product_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items')

    def __str__(self):
        return f"{self.product_name} ({self.quantity})"

# Task 4: BookMyShow-style Ticket model
class Ticket(models.Model):
    movie_title = models.CharField(max_length=100)
    seat_number = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')

    def __str__(self):
        return f"{self.movie_title} - {self.seat_number}"
