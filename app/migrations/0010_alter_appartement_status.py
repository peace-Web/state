# Generated by Django 4.2.3 on 2023-08-05 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_appartement_occupied_alter_appartement_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appartement',
            name='status',
            field=models.CharField(choices=[('Show', 'show'), ('Hide', 'hide')], default='show', max_length=50, null=True),
        ),
    ]