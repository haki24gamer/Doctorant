# Generated by Django 5.1.5 on 2025-05-12 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0007_alter_notification_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='date',
            new_name='date_creation',
        ),
        migrations.AddField(
            model_name='notification',
            name='commentaire',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='titre',
            field=models.CharField(default='Notification', max_length=200),
        ),
    ]
