# Generated by Django 4.0 on 2024-01-26 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_pager', '0002_remove_profile_mark_news_id_profile_mark_news_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='news_images/'),
        ),
    ]
