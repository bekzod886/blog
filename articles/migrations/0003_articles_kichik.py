# Generated by Django 3.2.5 on 2021-08-18 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_articles_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='kichik',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
