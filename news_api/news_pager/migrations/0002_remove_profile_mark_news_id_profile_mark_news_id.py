# Generated by Django 4.0 on 2024-01-26 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_pager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='mark_news_id',
        ),
        migrations.AddField(
            model_name='profile',
            name='mark_news_id',
            field=models.ManyToManyField(related_name='bookmarked_by', to='news_pager.News'),
        ),
    ]
