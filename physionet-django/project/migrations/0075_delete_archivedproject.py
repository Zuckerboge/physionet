# Generated by Django 4.1.10 on 2023-12-22 22:00

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("project", "0074_migrate_archived_to_active"),
    ]

    operations = [
        migrations.DeleteModel(
            name="ArchivedProject",
        ),
    ]
