# Generated by Django 5.1 on 2024-08-18 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='image',
            field=models.URLField(max_length=3000, null=True),
        ),
    ]
