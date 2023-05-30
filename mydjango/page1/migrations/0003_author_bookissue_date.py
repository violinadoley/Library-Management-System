# Generated by Django 4.2.1 on 2023-05-30 20:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('page1', '0002_bookreview_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorname', models.CharField(max_length=30)),
                ('authorID', models.IntegerField()),
                ('authoremail', models.EmailField(max_length=254)),
                ('no_of_works', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='bookissue',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
