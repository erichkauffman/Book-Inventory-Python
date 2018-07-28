from rest_framework import serializers
from inventory.models import Book

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title',
                  'author', 
                  'isbn',
                  'edition',
                  'printing',
                  'cover',
                  'year_printed',
                  'description',
                  'condition',
                  'date_puchased',
                  'location_puchased',
                  'amount_paid',
                  'sell_price',
                  'site_listed',
                  'shelf_location',
                  'removal_action',
                  'date_removed')