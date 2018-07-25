from django.db import models

class Books(models.Model):
    title = models.TextField()
    author = models.TextField()
    isbn = models.TextField()
    edition = models.SmallIntegerField()
    printing = models.SmallIntegerField()
    cover = models.SmallIntegerField()
    year_printed = models.SmallIntegerField()
    description = models.TextField(null=True, blank=True)
    condition = models.SmallIntegerField()
    date_purchased = models.DateField()
    location_purchased = models.TextField(null=True, blank=True)
    amount_paid = models.IntegerField()
    sell_price = models.IntegerField()
    site_listed = models.SmallIntegerField(null=True, blank=True)
    shelf_location = models.TextField()
    removal_action = models.NullBooleanField(null=True, blank=True)
    date_removed = models.DateTimeField(null=True, blank=True)
