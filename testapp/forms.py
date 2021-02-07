from django.forms import ModelForm
from testapp.models import Author, Book


class Bookform(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'price', 'auth']


class Authorform(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'l_name', 'address']
