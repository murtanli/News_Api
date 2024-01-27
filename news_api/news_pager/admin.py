from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Users, Category, News, Profile

class UsersAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Users._meta.fields]
    ordering = ('login',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]
    ordering = ('category',)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'text', 'date', 'image_preview','image', 'get_category')

    def image_preview(self, obj):
        # Отображение изображения в админке
        if obj.image:
            news_id = obj.pk
            url = reverse('get_news_image', args=[news_id])
            return format_html('<img src="{}" alt="Image" style="max-width: 100px; max-height: 100px;" />', url)
        return None

    image_preview.short_description = 'Image Preview'

    def get_category(self, obj):
        # Отображение категории в виде строки вместо ссылки
        return str(obj.category_id)

    get_category.short_description = 'Category'

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user_login', 'display_marked_news')

    def user_login(self, obj):
        return obj.user_id.login if obj.user_id else None

    def display_marked_news(self, obj):
        return ", ".join([news.title for news in obj.mark_news_id.all()])

    display_marked_news.short_description = 'Marked News'

admin.site.register(Users, UsersAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Profile, ProfileAdmin)
