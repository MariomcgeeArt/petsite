# Generated by Django 3.0.8 on 2020-07-15 23:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_name', models.CharField(max_length=50)),
                ('species', models.CharField(max_length=50)),
                ('breed', models.CharField(max_length=50)),
                ('weight_in_pounds', models.IntegerField(null=True)),
                ('Owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_appointment', models.DateField(blank=True, null=True)),
                ('duration_minutes', models.IntegerField(null=True)),
                ('special_instructions', models.CharField(max_length=100)),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pets.Pet')),
            ],
        ),
    ]
