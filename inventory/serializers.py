from rest_framework import serializers
from inventory.models import Book

class BookSerializer(serializers.ModelSerializer):
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
                  'date_purchased',
                  'location_purchased',
                  'amount_paid',
                  'sell_price',
                  'site_listed',
                  'shelf_location',
                  'removal_action',
                  'date_removed')
        #fields = '__all__'