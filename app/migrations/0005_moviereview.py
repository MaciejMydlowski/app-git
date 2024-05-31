# Generated by Django 3.2.25 on 2024-05-27 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_movieactors_moviegenres_watchedmovies'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('watchedMovies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.watchedmovies')),
            ],
        ),
    ]
