# Generated by Django 3.0.7 on 2021-02-09 06:20

import colorfield.fields
from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('color', colorfield.fields.ColorField(max_length=18)),
            ],
        ),
        migrations.CreateModel(
            name='ProblemLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500, verbose_name='описание проблемы')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='время добавления')),
                ('house_number', models.CharField(blank=True, max_length=50, verbose_name='номер дома')),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='добавлено пользователем')),
                ('county', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='places.County', verbose_name='район области')),
                ('place', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='places.Place', verbose_name='населённый пункт')),
                ('road', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='places.Road', verbose_name='дорога')),
                ('state_district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='places.StateDistrict', verbose_name='район города')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='problem_register.Status', verbose_name='статус проблемы')),
            ],
        ),
    ]