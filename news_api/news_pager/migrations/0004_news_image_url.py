# Generated by Django 4.0 on 2024-01-26 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_pager', '0003_news_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]