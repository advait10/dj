from django.shortcuts import render
from .forms import Bookform, Authorform
from .models import Book


# Create your views here.

def homepage(request):
    form = Bookform()
    a_form = Authorform()
    bk = Book.objects.all()
    return render(request, 'tapp/base.html', {'form': form, 'a_form': a_form, 'book': bk})
