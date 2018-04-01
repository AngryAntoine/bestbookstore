from django.contrib import admin

from .models import (Author,
                     Book,
                     RequestListener
                     )


class BookInline(admin.TabularInline):
    model = Book.authors.through
    extra = 0
    max_num = 2


class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = [
        BookInline,
               ]


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display_links = ['title']
    list_display = ('title', 'price', 'active')
    list_editable = ('price', 'active')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(RequestListener)
