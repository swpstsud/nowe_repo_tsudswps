# Generated by Django 5.1.4 on 2024-12-10 09:56

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folder_aplikacji', '0002_person_pseudonym'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stanowisko',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=80)),
                ('opis', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='person',
            name='pseudonym',
        ),
        migrations.AddField(
            model_name='person',
            name='pseudonim',
            field=models.CharField(default='', max_length=80),
        ),
        migrations.CreateModel(
            name='Osoba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=40)),
                ('nazwisko', models.CharField(max_length=60)),
                ('plec', models.IntegerField(choices=[(1, 'Kobieta'), (2, 'Mężczyzna'), (3, 'Inna')], default=3)),
                ('data_dodania', models.DateField(default=datetime.date.today)),
                ('stanowisko', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='folder_aplikacji.stanowisko')),
            ],
            options={
                'ordering': ['nazwisko'],
            },
        ),
    ]
