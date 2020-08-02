from django.contrib import admin
from .models import Category,Subject,Book,Profile

admin.site.register(Category)
admin.site.register(Subject)
admin.site.register(Book)
admin.site.register(Profile)