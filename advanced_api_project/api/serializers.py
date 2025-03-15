from rest_framework import serializers
import datetime
from .models import Book, Author 


# BookSerializer to serialize all the fields from the Book model
# and also validating the publication year making sure it 
# isn't from the future.
class BookSerializer(serializers.ModelSerializer):
    """Serializer for the Book model with validation."""

    def validate_publication_year(self, value):
        """Ensure the publication year is not in the future."""
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the Future.")
        return value 
    class Meta:
        model = Book
        fields = '__all__'

    # def validate(self, data):
    #     if datetime.now() > ['publication_year']:
    #         raise serializers.ValidationError("Books can't be from the future.")
    #     return data

# AuthorSerializer used to serializer the name of the author and it
# includes a nested Book serializer to include all the books
# written by a single author.
class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for the author model including nested books."""
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['name', 'books']

  
    
