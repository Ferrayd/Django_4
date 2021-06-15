from django.contrib import admin
from .models import Author, Category, Post, Comment

@admin.register(Author, Category, Post, Comment)
class AuthorAdmin(admin.ModelAdmin):
    pass

