from django.contrib import admin
from.models import Book,Author

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'price',]
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'l_name', 'address']


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)


# Register your models here.
