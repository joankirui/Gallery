# Generated by Django 3.2 on 2021-11-27 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=30)),
                ('image_description', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.category')),
                ('image_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.location')),
            ],
        ),
    ]