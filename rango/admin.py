from django.contrib import admin
from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile
# Register your models here.

class PageInline(admin.TabularInline):
    model = Page
    extre = 3

class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None , {'fields': ['name']}),
        ('content', {'fields': [ 'views', 'likes']})
    ]
    list_display = ('name', 'views')
    list_filter = ['views']
    inlines = [PageInline]
    prepopulated_fields = {'slug':('name',)}

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'views')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)