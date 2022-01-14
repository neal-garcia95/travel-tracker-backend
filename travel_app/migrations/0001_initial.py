# Generated by Django 4.0.1 on 2022-01-14 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TripEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='EntryDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_url', models.TextField()),
                ('body', models.TextField()),
                ('date', models.DateField()),
                ('tripEntry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entryDetails', to='travel_app.tripentry')),
            ],
        ),
    ]
