from django.db import models

class Books(models.Model):
    title = models.TextField()
    author = models.TextField()
    isbn = models.TextField()
    edition = models.SmallIntegerField()
    printing = models.SmallIntegerField()
    cover = models.SmallIntegerField()
    year_printed = models.SmallIntegerField()
    description = models.TextField()
    condition = models.SmallIntegerField()
    date_purchased = models.DateField()
    location_purchased = models.TextField()
    amount_paid = models.IntegerField()
    sell_price = models.IntegerField()
    site_listed = models.SmallIntegerField()
    shelf_location = models.TextField()
    removal_action = models.NullBooleanField()
    date_removed = models.DateTimeField()
