# Generated by Django 3.0.5 on 2021-06-01 23:52

from django.db import migrations, models
import django.db.models.manager
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('composer', models.TextField()),
                ('executor', models.TextField()),
                ('genre', models.TextField()),
                ('label', models.TextField()),
                ('nominations', models.TextField()),
                ('release_date', models.TextField()),
                ('songwriter', models.TextField()),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
