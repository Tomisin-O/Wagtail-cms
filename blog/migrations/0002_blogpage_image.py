# Generated by Django 3.0.7 on 2020-06-09 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image'),
        ),
    ]
